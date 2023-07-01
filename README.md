# spotify-to-youtube-music
A repository to develop my first api, that transfers a spotify playlist to an youtube music playlist :).  Doing my best to make a good gift to a very good friend. 

## First steps:

   ### Acess `requirements.txt` to install all the pip's you need to use this code

   1 - Get Client ID & Client Secret from spotify
   2 - Create a `.env` file, and create 2 variables: SPOTIPY_CLIENT_ID = "your_client_id", SPOTIPY_CLIENT_SECRET="your_client_secret". Both client data's will be necessary to get your playlist information to do the transference.
   3 - Get client ID & Client secret from google
   4- Create a `oauth.json`file e put the google credentials you got previously.
   5 - Open your Youtube Music page and press Ctrl + Shift + i to open the developer tools e go to `network`, find the POST Youtube Music request, it has to be `browse?` file, if you strugglin' to do it, you can use the filter searching for `browse`.
   6 - When you find it, copy the headers request, open the terminal and type `ytmusic browser`, paste it, and press Ctrl + D, it'll create a `browser.json` file that'll used to create the playlist in Youtube Music.


