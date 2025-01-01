import spotipy
from spotipy.oauth2 import SpotifyOAuth
import argparse
from rich import print

# Spotify API credentials
SPOTIFY_CLIENT_ID = 'your_client_id'
SPOTIFY_CLIENT_SECRET = 'your_client_secret'
SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback'

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-playback-state user-modify-playback-state user-read-currently-playing"
))

def play_track(track_name):
    results = sp.search(q=track_name, type='track', limit=1)
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[track_uri])
        print(f":musical_note: Playing [bold]{track_name}[/bold]")
    else:
        print(":warning: Track not found!")

def current_track():
    current = sp.current_playback()
    if current and current['is_playing']:
        track = current['item']
        print(f"Now playing: [bold]{track['name']}[/bold] by [italic]{track['artists'][0]['name']}[/italic]")
    else:
        print("No track currently playing.")

def main():
    parser = argparse.ArgumentParser(description="Spotify CLI Client")
    parser.add_argument('--play', help="Play a track by name")
    parser.add_argument('--current', action='store_true', help="Show the current track")
    args = parser.parse_args()

    if args.play:
        play_track(args.play)
    elif args.current:
        current_track()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
