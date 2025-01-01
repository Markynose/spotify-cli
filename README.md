> [!CAUTION]
> First of all, DONT TOUCH EVERYTHING IN THIS BRANCH!!!

## Spotify CLI Client

A lightweight and efficient Command-Line Interface (CLI) client for Spotify, built with Python. This tool allows you to search for tracks, play music, and control playback directly from the terminal.

---

## Features

- **Play Music**: Search and play tracks by name.
- **Show Currently Playing**: Display the current track and artist.
- **Control Playback**: Extend functionality with play, pause, skip, and more.

---

## Prerequisites

### 1. Spotify Developer Account

- Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create an application.
- Note down the `Client ID` and `Client Secret` provided for your application.

### 2. Install Python and Pip

Ensure you have Python 3.6 or higher installed. You can download it [here](https://www.python.org/downloads/).

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Markynose/spotify-cli.git
   cd spotify-cli
   ```

2. Install the required dependencies:
   ```bash
   pip install spotipy rich
   ```

3. Set up environment variables for your Spotify API credentials:
   ```bash
   export SPOTIFY_CLIENT_ID='your_client_id'
   export SPOTIFY_CLIENT_SECRET='your_client_secret'
   export SPOTIFY_REDIRECT_URI='http://localhost:8888/callback'
   ```

---

## Usage

### Playing a Track

Search and play a track by name:
```bash
python spotify_cli.py --play "Track Name"
```

### Show Currently Playing Track

Display the currently playing track:
```bash
python spotify_cli.py --current
```

### Help

View all available commands:
```bash
python spotify_cli.py --help
```

---

## Configuration

- Ensure the Spotify API credentials are correctly set up in your environment.
- Customize the script by adding additional commands, such as skip, pause, or manage playlists.

---

## Dependencies

- [Spotipy](https://spotipy.readthedocs.io/) - Python client for the Spotify Web API.
- [Rich](https://rich.readthedocs.io/) - Library for terminal styling.

---

## License

This project is licensed under the GNU General Public License v3.0 License. See the [Licence](LICENSE) file for details.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## Author

Mark Buchok (me)

Happy listening!
