import requests
import pandas as pd

from data.utils import write_to_csv

url = 'https://raw.githubusercontent.com/gboeing/data-visualization/main/ncaa-football-stadiums/data/stadiums-geocoded.csv'


def parse_locations(url):
    locations = pd.read_csv(url)
    write_to_csv(locations, './csv/locations.csv')
    return locations

def test():
    loc_list = parse_locations(url)

