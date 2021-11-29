import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def make_plots(player, data, season):

    """
    Make plots to display for a given player based on their position.

    Inputs:
        - Player: Player name
        - data: Dataframe
        - season = season

    Output:
        - 4 Subplots for the given position

    """
    # Make a list of unique players
    players_list = data['Name'].unique().tolist()

    if player in players_list:
        visual = data[data['Name'] == player]
        position = visual.iloc[0]['Position']

        if position == 'QB':

            fig = make_subplots(rows=2, cols=2)
            # subplot_titles = ('Fantasy Points PPR', 'Rushing Yards', 'Passing Yards', 'Receiving Yards'))
            # Display fantasy points
            fig.add_trace(go.Scatter(name = 'Fantasy Points PPR', 
            x = visual['Week'],
            y = visual['FantasyPointsPPR'],
            fill = 'tozeroy'),
            row = 1,
            col = 1)
            # Display rushing yards
            fig.add_trace(go.Scatter(name = 'Rushing Yards',
            x = visual['Week'],
            y = visual['RushingYards'],
            fill = 'tozeroy'),
            row = 1,
            col = 2)
            # Display receiving yards
            fig.add_trace(go.Scatter(name = 'Passing Yards',
            x = visual['Week'],
            y = visual['PassingYards'],
            fill = 'tozeroy'),
            row = 2,
            col = 1)
            # Display passing yards
            fig.add_trace(go.Bar(name = 'Touchdowns',
            x = visual['Week'],
            y = visual['TotalTouchdowns']),
            row = 2,
            col = 2)
            
                # Update xaxis properties
            fig.update_xaxes(title_text="Week", row=1, col=1)
            fig.update_xaxes(title_text="Week", row=1, col=2)
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
            return st.plotly_chart(fig, use_container_width=True)

        elif position == 'WR':

            fig = make_subplots(rows=2, cols=2)
            # subplot_titles = ('Fantasy Points PPR', 'Rushing Yards', 'Passing Yards', 'Receiving Yards'))
            # Display fantasy points
            fig.add_trace(go.Scatter(name = 'Fantasy Points PPR', 
            x = visual['Week'],
            y = visual['FantasyPointsPPR'],
            fill = 'tozeroy'),
            row = 1,
            col = 1)
            # Display rushing yards
            fig.add_trace(go.Scatter(name = 'Receptions',
            x = visual['Week'],
            y = visual['Receptions'],
            fill = 'tozeroy'),
            row = 1,
            col = 2)
            # Display receiving yards
            fig.add_trace(go.Scatter(name = 'Receiving Yards',
            x = visual['Week'],
            y = visual['ReceivingYards'],
            fill = 'tozeroy'),
            row = 2,
            col = 1)
            # Display passing yards
            fig.add_trace(go.Bar(name = 'Touchdowns',
            x = visual['Week'],
            y = visual['TotalTouchdowns']),
            row = 2,
            col = 2)
            
                # Update xaxis properties
            fig.update_xaxes(title_text="Week", row=1, col=1)
            fig.update_xaxes(title_text="Week", row=1, col=2)
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
            return st.plotly_chart(fig, use_container_width=True)


        elif position == 'RB':

            fig = make_subplots(rows=2, cols=2)
            # subplot_titles = ('Fantasy Points PPR', 'Rushing Yards', 'Passing Yards', 'Receiving Yards'))
            # Display fantasy points
            fig.add_trace(go.Scatter(name = 'Fantasy Points PPR', 
            x = visual['Week'],
            y = visual['FantasyPointsPPR'],
            fill = 'tozeroy'),
            row = 1,
            col = 1)
            # Display rushing yards
            fig.add_trace(go.Scatter(name = 'Rushing Yards',
            x = visual['Week'],
            y = visual['RushingYards'],
            fill = 'tozeroy'),
            row = 1,
            col = 2)
            # Display receiving yards
            fig.add_trace(go.Scatter(name = 'Receiving Yards',
            x = visual['Week'],
            y = visual['ReceivingYards'],
            fill = 'tozeroy'),
            row = 2,
            col = 2)
            # Display passing yards
            fig.add_trace(go.Bar(name = 'Touchdowns',
            x = visual['Week'],
            y = visual['TotalTouchdowns']),
            row = 2,
            col = 1)
            
                # Update xaxis properties
            fig.update_xaxes(title_text="Week", row=1, col=1)
            fig.update_xaxes(title_text="Week", row=1, col=2)
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
            return st.plotly_chart(fig, use_container_width=True)

        elif position == 'TE':

            fig = make_subplots(rows=2, cols=2)
            # subplot_titles = ('Fantasy Points PPR', 'Rushing Yards', 'Passing Yards', 'Receiving Yards'))
            # Display fantasy points
            fig.add_trace(go.Scatter(name = 'Fantasy Points PPR', 
            x = visual['Week'],
            y = visual['FantasyPointsPPR'],
            fill = 'tozeroy'),
            row = 1,
            col = 1)
            # Display rushing yards
            fig.add_trace(go.Scatter(name = 'Rushing Yards',
            x = visual['Week'],
            y = visual['RushingYards'],
            fill = 'tozeroy'),
            row = 1,
            col = 2)
            # Display receiving yards
            fig.add_trace(go.Scatter(name = 'Receiving Yards',
            x = visual['Week'],
            y = visual['ReceivingYards'],
            fill = 'tozeroy'),
            row = 2,
            col = 1)
            # Display passing yards
            fig.add_trace(go.Bar(name = 'Touchdowns',
            x = visual['Week'],
            y = visual['TotalTouchdowns']),
            row = 2,
            col = 2)
            
                # Update xaxis properties
            fig.update_xaxes(title_text="Week", row=1, col=1)
            fig.update_xaxes(title_text="Week", row=1, col=2)
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
            return st.plotly_chart(fig, use_container_width=True)

        else:

            fig = make_subplots(rows=2, cols=2)
            # subplot_titles = ('Fantasy Points PPR', 'Rushing Yards', 'Passing Yards', 'Receiving Yards'))
            # Display fantasy points
            fig.add_trace(go.Bar(name = 'Fantasy Points PPR', 
            x = visual['Week'],
            y = visual['FantasyPointsPPR']),
            row = 1,
            col = 1)
            # Display rushing yards
            fig.add_trace(go.Bar(name = 'Field Goals Made',
            x = visual['Week'],
            y = visual['FieldGoalsMade']),
            row = 1,
            col = 2)
            # Display receiving yards
            fig.add_trace(go.Bar(name = 'Extra Points Made',
            x = visual['Week'],
            y = visual['ExtraPointsMade']),
            row = 2,
            col = 2)
            # Display passing yards
            fig.add_trace(go.Bar(name = 'Field Goal Completion Percentage',
            x = visual['Week'],
            y = visual['FieldGoalsMade'] / visual['FieldGoalsAttempted']),
            row = 2,
            col = 1)
            
                # Update xaxis properties
            fig.update_xaxes(title_text="Week", row=1, col=1)
            fig.update_xaxes(title_text="Week", row=1, col=2)
            fig.update_xaxes(title_text="Week", row=2, col=1)
            fig.update_xaxes(title_text="Week", row=2, col=2)

            fig.update_layout(template = 'plotly_dark', 
            title = {'text': f'{player} fantasy output by week for the {season}-{season + 1} season.',
            'y': 0.9,
            'x': 0.135,
            'yanchor': 'top',
            'xanchor': 'left'},
            height = 600,
            width = 1000,
            )
            return st.plotly_chart(fig, use_container_width=True)

    else:
        return st.subheader(f"It doesn't look like '{player}' has played any games this season.  Won't be able to provide \
        a valid prediction.  Try somebody else.")