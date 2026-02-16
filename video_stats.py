import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "MrBeast"
maxResults=50
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

def get_video_ids(playlistId):
    video_ids = []
    
    page_token = None
    
    base_url=f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId={playlistId}&key={API_KEY}"
    
    try:
        while True:
            url = base_url
            
            if page_token:
                url += f"&pageToken={page_token}" 
                
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        
            for item in data.get('items',[]):
                video_id = item['contentDetails']['videoId']
                video_ids.append(video_id)
            
            page_token = data.get('nextPageToken')
            
            if not page_token:
                break
        return video_ids
    
    except requests.exceptions.RequestException as e :
        raise e
        

if __name__ == "__main__":
    playlistId = get_playlist_id()
    print(get_video_ids(playlistId))
    
else:
    print("get_playlist_id wont be executed")