import requests
import json

from datetime import datetime
from zoneinfo import ZoneInfo

from data.utils import write_to_csv

YEAR = 2024

def get_scores():
    # ESPN API endpoint for college football scores
    url = f"http://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard"

    # Parameters for the request
    params = {
        "dates": YEAR,
        "groups": 80,
        "limit": 1000  # Adjust this value based on your needs
    }

    # Send GET request to the API
    return requests.get(url, params=params).text

def parse_scores(scores):
    data = json.loads(scores)

    # Extract and return the relevant score information
    scores = []
    for event in data['events']:
        game_date = datetime.strptime(event['date'], "%Y-%m-%dT%H:%M%z")
        season_type = event['season']['type']
        if game_date < datetime.now(ZoneInfo("UTC")) and season_type in [2, 3]:
            season_type = event['season']['type']
            season_year = event['season']['year']
            week_num = event['week']['number']
            game_date = str(game_date)
            home_team_id = event['competitions'][0]['competitors'][0]['id']
            home_team_name = event['competitions'][0]['competitors'][0]['team']['displayName']
            home_team_score = event['competitions'][0]['competitors'][0]['score']
            away_team_id = event['competitions'][0]['competitors'][1]['id']
            away_team_name = event['competitions'][0]['competitors'][1]['team']['displayName']
            away_team_score = event['competitions'][0]['competitors'][1]['score']
            winner_team_id = home_team_id if event['competitions'][0]['competitors'][0].get('winner') else away_team_id
            winner_team_name = home_team_name if event['competitions'][0]['competitors'][0].get(
                'winner') else away_team_name
            loser_team_id = away_team_id if not event['competitions'][0]['competitors'][1].get(
                'winner') else home_team_id
            loser_team_name = away_team_name if not event['competitions'][0]['competitors'][1].get(
                'winner') else home_team_name

            scores.append({
                'season_type': season_type,
                'season_year': season_year,
                'week_num': week_num,
                'game_date': game_date,
                'home_team_id': home_team_id,
                'home_team_name': home_team_name,
                'home_team_score': home_team_score,
                'away_team_id': away_team_id,
                'away_team_name': away_team_name,
                'away_team_score': away_team_score,
                'winner_team_id': winner_team_id,
                'winner_team_name': winner_team_name,
                'loser_team_id': loser_team_id,
                'loser_team_name': loser_team_name
            })
    return scores

def test():
    scores = get_scores()
    print(parse_scores(scores))
    # write_to_csv(scores, f"./csv/scores-{YEAR}.csv")

