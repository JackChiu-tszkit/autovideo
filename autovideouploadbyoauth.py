import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
CLIENT_SECRETS_FILE = 'client_secret.json'  # 你的API密钥文件

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=8080)
    return credentials

def upload_video(video_path, title, description, category_id):
    credentials = authenticate()
    youtube = build('youtube', 'v3', credentials=credentials)

    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'categoryId': category_id,
        },
        'status': {
            'privacyStatus': 'public',  # 或者 'private'，视需求而定
        },
    }

    media_file = MediaFileUpload(video_path, resumable=True)
    insert_request = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
    )

    response = None
    while response is None:
        status, response = insert_request.next_chunk()
        if status:
            print(f'Uploaded {int(status.progress() * 100)}%')

    print(f'Video uploaded! Video ID: {response["id"]}')

if __name__ == '__main__':
    video_path = 'path/to/your/video.mp4'  # 替换成你本地视频文件的路径
    title = 'Your Video Title'
    description = 'Your video description'
    category_id = '22'  # 22 表示 People & Blogs，你可以根据需要更改

    upload_video(video_path, title, description, category_id)
