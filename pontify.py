import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webpaige as ww
import os
from dotenv import load_dotenv

load_dotenv()

clientId = os.getenv("CLIENTID")
clientSecret = os.getenv("CLIENTSECRET")
dirPath = os.getenv("DIRPATH")
playlistID = "0IY8GvmliIB6m0hCy8YJGZ"
names=[]
tracks=[]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=clientId,
        client_secret=clientSecret,
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="playlist-read-private playlist-read-collaborative"
    )
)

playlist_url = "https://open.spotify.com/playlist/" + playlistID
results = sp.playlist_items(playlistID,limit=100,offset=0)

tracks.extend(results["items"])

while results["next"]:
    results = sp.next(results)
    tracks.extend(results["items"])
    
for item in tracks:
    track = item["track"]
    if track:
        names.append(dict(name = track["name"], artists = track["artists"][0]["name"]))

# with open("text.txt",'w') as f:
#     for i in names:
#         f.write(i["name"]+'-'+i['artists']+'.mp3'+'\n')

# ww.downloadCunt(names,dirPath)

print("done")
