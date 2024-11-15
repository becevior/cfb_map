import pandas as pd

def run_shit():
    groups = pd.read_csv('./csv/groups.csv')
    locations = pd.read_csv('./csv/locations.csv')
    scores = pd.read_csv('./csv/scores-2024.csv')
    team = pd.read_csv('./csv/team.csv')
    teams = pd.read_csv('./csv/teams.csv')

    new = (teams.merge(team, left_on='id', right_on='id')
           .merge(groups, left_on='group_id', right_on='group_id')
           .merge(locations, left_on='location', right_on='team', how='left'))
    return new

def test():
    print(run_shit().to_csv('./csv/test.csv'))