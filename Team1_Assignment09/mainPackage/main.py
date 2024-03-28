# main.py

import requests

url = "https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBTeamRoster"

querystring = {"teamAbv":"CHW","getStats":"true"}

headers = {
    "X-RapidAPI-Key": "894022e47emsh03029ed244790f4p1aba49jsn06684cbe4ee2",
    "X-RapidAPI-Host": "tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())


