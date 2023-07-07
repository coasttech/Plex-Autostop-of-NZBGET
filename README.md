# Tautulli Plex Stream-Based NZBGet Auto-Pause Script

This repository contains a Python script that utilizes Tautulli to monitor streaming activity in Plex and automatically pauses NZBGet when active streams are detected.

## Features

- Monitors Plex streams in real-time using Tautulli API
- Pauses NZBGet when active streams are detected
- Resumes NZBGet when streams end
- Configurable checking interval (30 seconds by default)
- Customizable Tautulli and NZBGet settings

## Requirements

- Python 3.x
- Dependencies: requests, base64

## Usage

1. Install Python 3.x if not already installed.
2. Install required dependencies using pip:
3. Clone or download the repository to your local machine.
4. Update the following settings in the script:
- Tautulli API key (`tautulli_apikey`)
- Tautulli URL (`tautulli_url`)
- NZBGet username (`nzbget_username`)
- NZBGet password (`nzbget_password`)
- NZBGet URL (`nzbget_url`)
5. Run the script using Python:
3. Clone or download the repository to your local machine.
4. Update the following settings in the script:
- Tautulli API key (`tautulli_apikey`)
- Tautulli URL (`tautulli_url`)
- NZBGet username (`nzbget_username`)
- NZBGet password (`nzbget_password`)
- NZBGet URL (`nzbget_url`)
5. Run the script using Python:

## Contributing

Contributions are welcome! If you have any improvements or new features to suggest, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
