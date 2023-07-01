import spotipy
import os
from dotenv import load_dotenv
from ytmusicapi import YTMusic

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
spotify_auth_manager =spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify_client = spotipy.Spotify(auth_manager=spotify_auth_manager)
resp = spotify_client.playlist_items("237GccrBGv1x6qLyn4gtLS")
items = resp["items"]

ytmusic = YTMusic("browser.json")
musicIds = []

for item in items:
    music_title = item["track"]["name"]
    album_name = item["track"]["album"]["name"]
    artists = item["track"]["artists"]
    artists_name = " ".join([a["name"] for a in artists if a["type"] == "artist"])
    query = f"{music_title} {artists_name} {album_name}"
    search_results = ytmusic.search(query)
    
    found_video_id = False
    for result in search_results:
        if "videoId" in result:
            music_id = result["videoId"]    # Get the video ID from the currente music
            print("Found sucessfully: \n")
            print(f"Title: {music_title}\n")  # Print in terminal the informations of the current music just to check if it's working
            print(f"Album: {album_name}\n")
            print(f"Artists: {artists_name}\n")
            print(f"YouTube Music ID: {music_id}\n")
            print("-" * 30 + "\n")
            found_video_id = True
            musicIds.append(music_id)  # Adiciona a ID de vídeo à lista musicIds
            break
    
    if not found_video_id:
        print("Search failed \n")
        print(f"The music '{music_title}' does not have a id.\n")
        print("-" * 30 + "\n")

new_playlist = ytmusic.create_playlist("azul indigo", "#3a7d9a musics!")
if musicIds:
    ytmusic.add_playlist_items(new_playlist, musicIds)
    print("Musics added to the Youtube playlist sucessfully")
else:
    print("No musics has been found to be added to the Youtube playlist")