from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import pandas as pd

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes)
    auth_base64_string = auth_base64.decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64_string,
        "Content-Type" : "application/x-www-form-urlencoded"
        }
    
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url  + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    return json_result[0]

def get_songs_by_EHNA(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=FR"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def get_artist_albums(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = get_auth_header(token)
    params = {
        "include_groups": "album,single",
        "limit": 50  # can paginate if needed
    }
    result = get(url, headers=headers, params=params)
    json_result = json.loads(result.content)["items"]
    
    filtered = [x for x in json_result if x["total_tracks"] > 1]
    return filtered

def get_album_track(token, album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["items"]
    return json_result

def get_track_info(token, track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

token = get_token()
result = search_for_artist(token, "ENHYPEN")
artist_id = result["id"]

albums = get_artist_albums(token, artist_id)

popularity_scores = []

for idx, album in enumerate(albums):
    album_id = album["id"]
    album_name = album["name"]
    tracks = get_album_track(token, album_id)
    for idx, track in enumerate(tracks):
        track_id = track["id"]
        track_name = track["name"]
        popularity = get_track_info(token, track_id)
        track_popularity = popularity["popularity"]
        popularity_scores.append([album_name, track_name, track_popularity])
    
df = pd.DataFrame(popularity_scores, columns=["album", "track", "popularity"])
df.to_csv("spotify_popularity_scores.csv", index=False)