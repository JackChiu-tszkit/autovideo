from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

API_KEY = ''  # 替换成你的 API 密钥
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def upload_video(video_path, title, description, category_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

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
    videos_insert_response = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
    ).execute()

    print(f'Video uploaded! Video ID: {videos_insert_response["id"]}')

if __name__ == '__main__':
    video_path = '/Users/jchiu/Downloads/Unraveling the Historical Tensions between Israel and Palestine.mp4'  # 替换成你本地视频文件的路径
    title = 'Your Video Title'
    description = 'Your video description'
    category_id = '22'  # 22 表示 People & Blogs，你可以根据需要更改

    upload_video(video_path, title, description, category_id)
