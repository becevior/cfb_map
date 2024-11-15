import json

import requests
import pandas as pd

from data.utils import write_to_csv

TEAMS_URL = 'https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams?limit=1000'

def get_teams():
    response = requests.get(TEAMS_URL)
    return response.json()['sports'][0]['leagues'][0]['teams']

def parse_teams(teams_data):
    teams = []
    for team in teams_data:
        json_data = team['team']
        json_data.pop('links', None)
        teams.append(json_data)
    return teams

def test():
    teams = get_teams()
    parsed = parse_teams(teams)
    write_to_csv(parsed, './csv/teams.csv')