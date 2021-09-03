import requests
import json
import time

showId = 'XXX' # enter the show id that you want to mark as played
episodeID = 'XXX' # enter the episode id that you want to start with
deviceID = 'XXX' # enter your device id (https://api.spotify.com/v1/me/player/devices)
authToken = 'XXX' # enter your auth token with user-modify-playback-state permissions
order = 'ASC' # enter 'ASC' if the episodes return oldest to newest or 'DESC' if they return newest to oldest
pad = 200*1000 # enter any padding in miliseconds that you want to add

headers = {
     'Accept': 'application/json',
     'Content-Type': 'application/json',
     'Authorization': 'Bearer ' + authToken
}

url = 'https://api.spotify.com/v1/shows/' + showId + '/episodes?market=US'
if order == 'DESC':
    markPlayed = False
else:
    markPlayed = True
offset = 0
while url:
    response = requests.get(url, headers=headers)
    print(response)
    episodes = response.json().get('items')
    for episode in episodes:
        if order == 'DESC':
            position = int(response.json().get('total')) - offset - 1
        else:
            position = offset
        if episode.get('id') == episodeID:
            if order == 'DESC':
                markPlayed = True
            else:
                markPlayed = False
        if markPlayed == True:
            data = '{"context_uri":"spotify:show:' + showId + '","offset":{"position":' + str(position) + '},"position_ms":' + str(episode.get('duration_ms')+pad) + '}'
            play_response = requests.put('https://api.spotify.com/v1/me/player/play?device_id=' + deviceID, headers=headers, data=data)
            time.sleep(2)
            print(str(position) + '      ' + episode.get('name'))
            print(play_response)
        offset = offset + 1
    url = response.json().get('next')
