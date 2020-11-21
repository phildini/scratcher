import os
import random

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(BASE_DIR, ".env"))

all_titles = []
page = 1
more = True
while more:
    resp = requests.get(f"https://itch.io/my-purchases?page={page}&format=json", headers={'Cookie': os.environ["ITCH_COOKIE"]})
    if resp.json()['num_items'] != 50:
    soup = BeautifulSoup(resp.json()['content'], 'html.parser')
    titles = soup.find_all("div", "game_title")
    games = soup.find_all("div", "game_cell")
    all_titles += [game.find("div", "game_title").text for game in games if game.find("span", "icon-apple")]
    page += 1

print(random.choice(all_titles))
