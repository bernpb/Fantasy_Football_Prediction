import pandas as pd
import numpy as np
import streamlit as st
import time
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from Project_Functions import trailing_stats_single_column, trailing_stats_mean, get_contribution
from Project_Functions import get_tiers, get_touchdowns, get_yards, tier_maker, LogShift, DenseTransformer


# Define some variables
week = 12
season = 2021
im = Image.open('Docs/.ipynb_checkpoints/ameer-basheer-Yzef5dRpwWg-unsplash.jpg')
im2 = Image.open('Docs/.ipynb_checkpoints/ben-hershey-B4XZxcZcTsI-unsplash.jpg')

# Set the default width of the app
# st.set_page_config(layout='wide')

# Build out the sidebar

st.sidebar.image(im)
st.sidebar.write('')
st.sidebar.write('This page is the result of my final project for the Lighthouse Labs data science \
    bootcamp.  \n It is intended for demonstration purposes only.  Please do not share the link to this \
        page without permision.  Please see my contact info below if you would like to get in touch.')
st.sidebar.markdown('**********')
st.sidebar.subheader('Contact')
st.sidebar.write('Bern Priest-Blais')
st.sidebar.write('bern.priestblais@gmail.com')
st.sidebar.markdown('*********')
st.sidebar.subheader('Project Repo')
st.sidebar.write('https://github.com/bernpb/LHL_Final_Project')

# Header
st.title('NFL Fantasy Point Projections')
st.markdown('*************')
st.subheader(f"Week {week} ")
st.subheader(f'{season}-{season + 1} season')
st.image(im2)
st.write('\n \n')
description = 'This is a machine learning model designed to predict the offensive output of NFL players on a weekly basis. <br> <br>\
    Valid positions for prediction are: <br> \
        - Quarterback (QB) <br>\
        - Running Back (RB) <br>\
        - Wide Receiver (WR) <br>\
        - Tight End (TE) <br>\
        - Kicker (K) <br>'
st.markdown(description, unsafe_allow_html=True)
st.markdown('***********')
st.write("To start, enter the name of the player you are looking for projections \
            for in the box  below.  (Case and spelling matter) ")

# Prompt for player input            
player = st.text_input('Player Name', 'Tom Brady')

@st.cache(allow_output_mutation=True)
def generate_data(df_players, df_schedule, week, season):
    
    """
    Use this function to generate a dataframe of games yet to happen to make a prediction.  
    
    Inputs:
        - df_players: Dataframe of player statistics from previous weeks.
        - df_schedule: Dataframe of team schedules
        - week: Week of the season we want to generate data for
        - season: Season we want to generate the data for
        
    Output:
        - Dataframe in the same format as df_players that can be used for predictions
    """
    
    # Build a dictionary of players and their teams for the current season.
    # This is meant to represent the active roster of players for predictions

    # Create a view of the dataframe with just the player and his associated team name 
    df_active = df_players[df_players['Season'] == season][['Name', 'Team']]

    # Create a dictionary with player as the key and team as the value
    active_players = {}
    for i, row in enumerate(range(len(df_active))):
        active_players[df_active.iloc[i]['Name']] = df_active.iloc[i]['Team']
        
    # Get the slate of games for the week in question
    df_schedule_week_season = df_schedule[(df_schedule['Week'] == week) & (df_schedule['Season'] == season)]
    
    # Create a dictionary of matchups for the week
    matchup_dict = {}
    for i, row in enumerate(range(len(df_schedule_week_season))):
        matchup_dict[df_schedule_week_season.iloc[i]['HomeTeam']] = df_schedule_week_season.iloc[i]['AwayTeam']
        matchup_dict[df_schedule_week_season.iloc[i]['AwayTeam']] = df_schedule_week_season.iloc[i]['HomeTeam']
    
    

    # Make a list of the columns in df_players to create a new dataframe with the same info
    columns = df_players.columns.tolist()

    # Build out rows of a dataframe with players and their associated games
    df_predictions = pd.DataFrame(columns = columns)
    for ele in active_players.keys():
        if active_players[ele] in matchup_dict.keys():
            df_predictions = df_predictions.append({'Name': ele,
                                                    'Team': active_players[ele],
                                                   'Opponent': matchup_dict[active_players[ele]]},
                                 ignore_index = True)
        else:
            pass
    df_predictions['Week'] = week # Fill the week column
    df_predictions['Season'] = season # Fill the season column
    
    # Append the last 8 weeks of play to df_predictions so that the trailing fantasy points can be calculated
    data = df_players[(df_players['Season'] == season)].append(df_predictions).reset_index()
    data = get_touchdowns(data)
    data = get_yards(data)
    
    # Calculate trailing fantasy points for the week in question
    data = trailing_stats_single_column(data, 'FantasyPointsPPR')
    
    return data


# Import the model for prediction
import pickle
model = pickle.load(open('Pickles/SVR.pickle', 'rb'))



# Import the datasets used to generate player data for future games
df_players = pd.read_csv('Data/weekly_data.csv')
df_schedule = pd.read_csv('Data/game_scores.csv')

# Generate data
data = generate_data(df_players, df_schedule, week, season)

players_list = data['Name'].unique().tolist()

if player in players_list:
    # Create a visualization
    visual = data[data['Name'] == player]
   
    fig = make_subplots(rows=2, cols=2,)
    # subplot_titles = ('Fantasy Points PPR', 'Rushing Yards', 'Passing Yards', 'Receiving Yards'))
    # Display fantasy points
    fig.add_trace(go.Bar(name = 'Fantasy Points PPR', 
    x = visual['Week'],
    y = visual['FantasyPointsPPR']),
    row = 1,
    col = 1)
    # Display rushing yards
    fig.add_trace(go.Bar(name = 'Rushing Yards',
    x = visual['Week'],
    y = visual['RushingYards']),
    row = 1,
    col = 2)
    # Display receiving yards
    fig.add_trace(go.Bar(name = 'Receiving Yards',
    x = visual['Week'],
    y = visual['ReceivingYards']),
    row = 2,
    col = 2)
    # Display passing yards
    fig.add_trace(go.Bar(name = 'Passing Yards',
    x = visual['Week'],
    y = visual['PassingYards']),
    row = 2,
    col = 1)
    
        # Update xaxis properties
    fig.update_xaxes(title_text="Week", row=1, col=1)
    fig.update_xaxes(title_text="Week", range=[0, 12], row=1, col=2)
    fig.update_xaxes(title_text="Week", row=2, col=1)
    fig.update_xaxes(title_text="Week", row=2, col=2)

    fig.update_layout(template = 'plotly_dark',
    title = {'text': f'{player} fantasy output by week for the {season}-{season + 1} season.',
    'y': 0.9,
    'x': 0.135,
    'yanchor': 'top',
    'xanchor': 'left'},
    height = 600,
    width = 1000)
    st.plotly_chart(fig, use_container_width=True)


else:
    st.subheader(f"It doesn't look like '{player}' has played any games this season.  Won't be able to provide \
        a valid prediction.  Try somebody else.")

# Generate predictions for the dataset
@st.cache
def get_predictions(model, data):
    preds = model.predict(data)
    return np.exp(preds) - 10


# Calculate the predictions for all week 12 players
with st.spinner('Crunching numbers, delivering you to glory......'):
    data['Prediction'] = get_predictions(model, data)

    # If the player is playing, get their predicted output
    try:
        predicted_output = round(float(data[(data['Week'] == week) & (data['Name'] == player)][['Prediction']].values[0][0]),2)
    # If bye week, say so
    except:
        predicted_output = 'Bye Week'

    # Format the output for the player
    col1, col2 = st.columns(2)
    col1.metric('Player', player)
    col2.metric('Predicted Points', predicted_output)
st.success('Enjoy thrashing your buddies.')