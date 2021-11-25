import pandas as pd
import numpy as np
from Project_Functions import trailing_stats_single_column


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
    df_active

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
    data.drop(columns = 'FantasyPointsPPR',
             inplace = True)
    
    return data