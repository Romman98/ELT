import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():

    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails%20&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        output = json.dumps(data,indent=2)
        # print(output)
        channel_items = data["items"][0]
        channel_playlistsId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        print(channel_playlistsId)
        return channel_playlistsId
    except requests.exceptions.RequestException as e :
        raise e
    
if __name__ == "__main__":
    get_playlist_id()
else:
    print("get_playlist_id wont be executed")