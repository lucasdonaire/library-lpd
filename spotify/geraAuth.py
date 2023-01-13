
import spotipy

sp = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyOAuth(
        client_id='3a92f783c17f4b95bc75d536dc51be3d',
        client_secret='89e6b1f4d2914d158a34c71f71190d2f',
        redirect_uri="https://localhost:8000/callback",
        scope="user-library-read playlist-modify-public user-library-modify playlist-modify-private user-top-read"
        )
    )

sp.current_user_saved_tracks()