# main.py

# Name: Team #1 (Harsh Shah, Ian Cunningham, and Elizabeth Stapleton)
# email: shahh4@mail.uc.edu, stapleet@mail.uc.edu, cunninig@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/04/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment:
# Anything else that's relevant: Used worked done in class as a reference. 
'''
import requests

if __name__ == "__main__":

    url = "https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBTeamRoster"
    
    querystring = {"teamAbv":"CHW","getStats":"true"}
    
    headers = {
        "X-RapidAPI-Key": "894022e47emsh03029ed244790f4p1aba49jsn06684cbe4ee2",
        "X-RapidAPI-Host": "tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
    
        # Extracting player information
        players = data.get('players', [])
        
        # Printing player names and positions
        print("weight:")
        for player in players:
            weight = player.getStats('weight', 'Unknown')
            #position = player.get('primaryPosition', 'Unknown')
            print(f"Weight: {weight}")
    else:
        print(f"Failed to retrieve data from the API. Status code: {response.status_code}")
        print(f"Error message: {response.text}")
    
    
    
    #print(response.json['height'])

'''
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
        
        # Initialize variables to store the heaviest player information
        heaviest_player_name = ""
        heaviest_player_weight = 0
        
        # Iterate through the players to find the heaviest one
        for player in players:
            weight = player.get('weight', 0)
            if weight > heaviest_player_weight:
                heaviest_player_name = player.get('fullName', 'Unknown')
                heaviest_player_weight = weight
        
        # Print the heaviest player's information
        if heaviest_player_name:
            print(f"The heaviest player is {heaviest_player_name} with a weight of {heaviest_player_weight} lbs.")
        else:
            print("No player information available.")
    else:
        print(f"Failed to retrieve data from the API. Status code: {response.status_code}")
        print(f"Error message: {response.text}")


