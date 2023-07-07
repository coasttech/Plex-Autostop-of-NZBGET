import requests
import base64
import time

# Tautulli settings
tautulli_apikey = 'Your Tautulli API key'
tautulli_url = 'http://localhost:8181'  # Update with your Tautulli IP and port

# NZBGet settings
nzbget_username = 'Your NZBGet username'
nzbget_password = 'Your NZBGet password'
nzbget_url = 'http://localhost:6789'  # Update with your NZBGet IP and port

# Basic Authentication string for NZBGet
nzbget_auth = base64.b64encode(f"{nzbget_username}:{nzbget_password}".encode()).decode()

# Function to check if streaming is happening
def check_plex_streaming():
    # Tautulli API endpoint for getting stream details
    url = f"{tautulli_url}/api/v2?apikey={tautulli_apikey}&cmd=get_activity"
    response = requests.get(url)

    # Decoding the JSON response
    data = response.json()

    # Checks if there are any streams
    if int(data['response']['data']['stream_count']) > 0:
        print("Streaming detected. Stopping NZBGet.")
        # Pauses NZBGet if a stream is detected
        pause_nzbget()
    else:
        print("No streams detected. Starting NZBGet.")
        # Unpauses NZBGet if no stream is detected
        unpause_nzbget()

# Function to pause NZBGet
def pause_nzbget():
    url = f"{nzbget_url}/jsonrpc/pause?username={nzbget_username}&password={nzbget_password}"
    response = requests.get(url)
    if response.status_code == 200:
        print("NZBGet paused successfully.")
    else:
        print("Error pausing NZBGet.")

# Function to unpause NZBGet
def unpause_nzbget():
    url = f"{nzbget_url}/jsonrpc/resume?username={nzbget_username}&password={nzbget_password}"
    response = requests.get(url)
    if response.status_code == 200:
        print("NZBGet resumed successfully.")
    else:
        print("Error resuming NZBGet.")

# While loop to continuously check for Plex streaming every 30 seconds
while True:
    check_plex_streaming()
    time.sleep(30)
