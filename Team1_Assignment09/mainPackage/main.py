# main.py
import requests

if __name__ == "__main__":
    url = "https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBTeamRoster"
    querystring = {"teamAbv": "CHW", "getStats": "true"}
    headers = {
        "X-RapidAPI-Key": "894022e47emsh03029ed244790f4p1aba49jsn06684cbe4ee2",
        "X-RapidAPI-Host": "tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        players = data.get('players', [])
        
        if players:
            heaviest_player_name = ""
            heaviest_player_weight = 0
            
            for player in players:
                weight = player.get('weight', 0)
                if weight > heaviest_player_weight:
                    heaviest_player_name = player.get('fullName', 'Unknown')
                    heaviest_player_weight = weight
            
            if heaviest_player_name:
                print(f"The heaviest player is {heaviest_player_name} with a weight of {heaviest_player_weight} lbs.")
            else:
                print("No heaviest player information available.")
        else:
            print("No player information available.")
    else:
        print(f"Failed to retrieve data from the API. Status code: {response.status_code}")
        print(f"Error message: {response.text}")