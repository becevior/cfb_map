import pandas as pd
import requests

from data.utils import write_to_csv

TEAM_URL = 'https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/'

def get_distinct_teams():
    df = pd.read_csv('./csv/teams.csv')
    return df.id.unique()

def get_team_info(team_ids):
    teams = []
    for team in team_ids:
        response = requests.get(f"{TEAM_URL}{team}")
        teams.append(response.json())
    return teams

def parse_team(teams):
    team_data = []
    for team in teams:
        data = team['team']
        team_data.append({
            "team_name": data['displayName'],
            "id": data['id'],
            "group_id": data['groups']['id'],
            "parent_group_id": data['groups'].get('parent', {}).get('id', '')
        })
    return team_data

def test():
    team_ids = get_distinct_teams()
    teams = get_team_info(team_ids)
    teams = parse_team(teams)
    write_to_csv(teams, './csv/team.csv')