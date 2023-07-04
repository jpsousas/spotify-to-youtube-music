# spotify-to-youtube-music
A repository to develop my first api, that transfers a spotify playlist to an youtube music playlist :).  Doing my best to make a good gift to a very good friend. 

## First steps:

1 - Run `pip install -r requirements.txt` to install python requirements
2 - Get Client ID & Client Secret from spotify
3 - Rename the `.env.example` file to `.env`, and fill 4 variables: SPOTIPY_CLIENT_ID = "your_client_id", SPOTIPY_CLIENT_SECRET="your_client_secret", YOUTUBE_COOKIE="your_youtube_cookie" SPOTIFY_PLAYLIST_LINK="your_spotify_playlist_link". 
4 - Open your Youtube Music page and press Ctrl + Shift + i to open the developer tools e go to `network`, find the POST Youtube Music request, it has to be `browse?` file, if you strugglin' to do it, you can use the filter searching for `browse`.
5 - When you find it, search for `headers` tab, look for request headers and find `cookies`, right click it and copy value. So paste it into your `YOUTUBE_COOKIE="your_youtube_cookie"` in your `.env` file.
6 - Run 
```console
jpsousas@note:~$ python3 spotify.py
```


