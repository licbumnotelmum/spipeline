import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENTID")
CLIENT_SECRET = os.getenv("CLIENTSECRET")
PLAYLIST_ID = "0IY8GvmliIB6m0hCy8YJGZ"

# 1. Get access token
auth = base64.b64encode(
    f"{CLIENT_ID}:{CLIENT_SECRET}".encode()
).decode()

token = requests.post(
    "https://accounts.spotify.com/api/token",
    headers={"Authorization": f"Basic {auth}"},
    data={"grant_type": "client_credentials"},
    timeout=10
).json()["access_token"]

# 2. Fetch playlist tracks
headers = {"Authorization": f"Bearer {token}"}
url = f"https://api.spotify.com/v1/playlists/{PLAYLIST_ID}/tracks"
params = {"limit": 50}

names = []
while url:
    r = requests.get(url, headers=headers, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    for item in data["items"]:
        track = item["track"]
        if track:
            names.append(dict(name = track["name"], artists = track["artists"][0]["name"]))

    url = data["next"]
    params = None
print(names)