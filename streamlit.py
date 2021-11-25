import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from Project_Functions import trailing_stats_single_column, trailing_stats_mean, get_contribution
from Project_Functions import get_tiers, get_touchdowns, get_yards, tier_maker, LogShift, DenseTransformer


# Define some variables
week = 12
season = 2021

# Header
st.title('NFL Fantasy Point Projections')
st.subheader(f"Predict Offensive Output of NFL Players for week {week} of the \
    {season}-{season + 1} season.")
st.write('\n \n')
st.write("To start, please enter the name of the player you are looking for projections \
            for in the box below.  (Case and spelling matter) ")



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
    
    # Calculate trailing fantasy points for the week in question
    data = trailing_stats_single_column(data, 'FantasyPointsPPR')
    
    return data


# Import the model for prediction
import pickle
model = pickle.load(open('Pickles/XGBoost.pickle', 'rb'))

# Prompt for player input            
player = st.text_input('Player Name', 'Tom Brady')

# Import the datasets used to generate player data for future games
df_players = pd.read_csv('Data/weekly_data.csv')
df_schedule = pd.read_csv('Data/game_scores.csv')

# Generate data
data = generate_data(df_players, df_schedule, week, season)

players_list = data['Name'].unique().tolist()

if player in players_list:
    # Create a visualization
    st.write(f'{player} fantasy output by week for the {season}-{season + 1} season.')
    alias = data
    visual = alias[alias['Name'] == player][['Week', 'FantasyPointsPPR', \
        ]].set_index('Week')
    st.line_chart(visual)

else:
    st.subheader(f"It doesn't look like '{player}' has played any games this season.  Won't be able to provide \
        a valid prediction.  Try somebody else.")

# Generate predictions for the dataset
def get_predictions(model, data):
    preds = model.predict(data)
    return np.exp(preds) - 10

data['Prediction'] = get_predictions(model, data)
predicted_output = data[(data['Week'] == week) & (data['Name'] == player)][['Name', 'Team','Week','Prediction']]
predicted_output