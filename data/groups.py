import json
import requests

from data.utils import write_to_csv

GROUP_URL = "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard/conferences?groups="
GROUPS = [57, 58, 80, 81]

def get_groups(group):
    params = {
        "group": 80,
        "limit": 1000  # Adjust this value to ensure all teams are retrieved
    }

    return requests.get(f"{GROUP_URL}{group}", params=params).text

def assemble():
    datas = []
    for group in GROUPS:
        data = json.loads(get_groups(group))['conferences']
        for d in data:
            datas.append({
                'group_id': d['groupId'],
                'name': d['name'],
                'logo': d.get('logo')
            })
    return datas

def test_assemble():
    groups = assemble()
    write_to_csv(groups, "./csv/groups.csv")
