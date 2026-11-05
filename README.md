# YouTube Video Uploader with Python

A Python-based tool for uploading videos to YouTube using the **YouTube Data API v3** and the Google API Python Client.

This project demonstrates how to automate video uploads, configure video metadata, and manage video visibility programmatically.

## P1 — Core Features

- Upload local video files to YouTube.
- Set custom video titles and descriptions.
- Assign YouTube video categories.
- Configure video visibility (`public`, `private`, or `unlisted`).
- Use resumable uploads for improved reliability.
- Retrieve the uploaded video's ID.

## 1. Prerequisites

Before running the script, ensure you have:

- Python 3.9 or later.
- A Google account with a YouTube channel.
- A Google Cloud project.
- YouTube Data API v3 enabled.
- OAuth 2.0 client credentials.

## 2. Installation

Install the required Python packages:

```bash
pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
```

Alternatively, create a `requirements.txt` file:

```text
google-api-python-client
google-auth-oauthlib
google-auth-httplib2
```

Then install:

```bash
pip install -r requirements.txt
```

## 3. Google Cloud Configuration

1. Open the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Navigate to **APIs & Services → Library**.
4. Search for **YouTube Data API v3** and enable it.
5. Configure the OAuth consent screen under **Google Auth Platform**.
6. Create an OAuth client ID for a desktop application.
7. Download the OAuth client configuration JSON file.
8. Save it as `client_secret.json` in your project directory.

**Important:** YouTube video uploads require OAuth 2.0 authentication. API keys alone cannot authorize video uploads.

## 4. Project Structure

```text
youtube-video-uploader/
├── README.md
├── requirements.txt
├── upload_video.py
├── client_secret.json
└── videos/
    └── sample_video.mp4
```

Do not commit `client_secret.json`, access tokens, or refresh tokens to a public GitHub repository.

Add the following to `.gitignore`:

```gitignore
client_secret.json
token.json
.env
__pycache__/
.venv/
```

## 5. Authentication with OAuth 2.0

Replace API-key authentication with OAuth 2.0 authentication.

```python
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth
