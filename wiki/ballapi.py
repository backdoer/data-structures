from urllib.request import urlopen, Request, URLError   #import these libraries in order to create the web requests, allowing you to pull data from an API
import requests                                         #The Request library allows you to easily use functions to write against APIs
import os
import csv
import collections
import time


api_key = 'z61uEjPdOSvBWAYteq5xaKypM7VG3r4b'

json_teams = []

#can easily define functions, the syntax of the language makes the code more easily readable
def get_teams(api_key):
    try:
            ############ GET TEAM OBJECT #########  # use the requests function to send the URL and payload
                #You can conveniently use a dictionary for your payload when using the requests object
        team_payload = {'api_key': api_key}
        teams = requests.post(
            'http://api.probasketballapi.com/team', data=team_payload)

        # create json object from http request for teams (actually a
        # list)
        json_teams = teams.json()

            # list with keys for teams
        team_keys = []

        for key in json_teams[0].keys():
            team_keys.append(key)

        teams = collections.namedtuple('Teams', ['keys', 'object'])
        team_items = teams(team_keys, json_teams)

    except:
        print('error')

    return team_items

def get_players(api_key):
    player_payload_setup = {'api_key': api_key}
    players = requests.post(
        'http://api.probasketballapi.com/player', data=player_payload_setup)

    json_players = players.json()
    
        # list with keys for players
    player_keys = []

        # set fieldnames for each key, append to fieldnames array

    for key in json_players[0].keys():
        player_keys.append(key)

    players = collections.namedtuple('Players', ['keys', 'object'])
    player_items = players(player_keys, json_players)

    return player_items   #You can also return multiple objects in Python  

def write_to_file(team_items, fieldnames):

        # Here we can see a csv writer being created in just a line of code. You can easily write a header for the file given a list
        # To create a CSV with Python all you need to do is to use the open function, and give it the required parameters, which are file name,
        # what you want to do with that file (update, write, read), and other parameters for style if needed. You then can write headers with a list,
        # and you can write the rows by passing in a list or a dictionary
    csvfile = open('names.csv', 'a', newline='')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
    writer.writeheader()

    ########## GET TEAMS AND PLAYERS AND PRINT IN CSV FILE #########
    for team in team_items[1]:
        player_payload = {'api_key': api_key, 'team_id': team['id']}
        players = requests.post(
            "http://api.probasketballapi.com/player", data=player_payload)

                # set json object for players
        json_player = players.json()
        for player in json_player:
                # Here, we are writing the actual data using dictionaries. The key references the header values, and then the value references data from 
                # lists I have created. 
            writer.writerow({'player_name': player['player_name'], 'last_name': player['last_name'], 'first_name': player['first_name'],
                             'birth_date': player['birth_date'], 'position': player['position'], 'team_id': player['team_id'], 'id': player['id'],
                             'dk_position': player['dk_position'], 'dk_id': player['dk_id'], 'team_name': team['team_name'], 'abbreviation': team['abbreviation'],
                             'city': team['city'], 'created_at': team['created_at'], 'updated_at': team['updated_at'], 'dk_id': team['dk_id']})


    #call functions
team_items = get_teams(api_key)
player_items = get_players(api_key)

    # create array with headers
field_headers = []

    # append headers to the field header array
field_headers += player_items.keys
field_headers += team_items.keys

write_to_file(team_items, field_headers)
