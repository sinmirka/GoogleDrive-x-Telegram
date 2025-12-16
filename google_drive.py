from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive.file"]
FOLDER_ID = "1Gzwz-hW1uJAfpwv2BNPdyy85HIdagVGr"

def upload_txt(filename: str):
    creds = Credentials.from_authorized_user_file(
        "token.json",
        scopes=SCOPES
    )

    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": [filename],
        "parents": [FOLDER_ID]
    }

    media = MediaFileUpload(
        filename=filename,
        mimetype="text/plain"
    )

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()
    print("File uploaded. ID:", file.get("id"))


def upload_image(filename: str):
    creds = Credentials.from_authorized_user_file(
        "token.json",
        scopes=SCOPES
    )

    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": [filename],
        "parents": [FOLDER_ID]
    }

    media = MediaFileUpload(
        filename=filename,
        mimetype="image/jpeg"
    )

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()
    print("File uploaded. ID:", file.get("id"))


def upload_doc(filename: str, mime_type: str):
    creds = Credentials.from_authorized_user_file(
        "token.json",
        scopes=SCOPES
    )

    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": [filename],
        "parents": [FOLDER_ID]
    }

    media = MediaFileUpload(
        filename=filename,
        mimetype=mime_type
    )

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()
    print("File uploaded. ID:", file.get("id"))


def upload_voice(filename: str, mime_type: str):
    creds = Credentials.from_authorized_user_file(
        "token.json",
        scopes=SCOPES
    )

    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": [filename],
        "parents": [FOLDER_ID]
    }

    media = MediaFileUpload(
        filename=filename,
        mimetype=mime_type
    )

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()
    print("File uploaded, type: voice, ID:", file.get("id"))


def upload_video_audio(filename: str, mime_type: str):
    creds = Credentials.from_authorized_user_file(
        "token.json",
        scopes=SCOPES
    )

    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": [filename],
        "parents": [FOLDER_ID]
    }

    media = MediaFileUpload(
        filename=filename,
        mimetype=mime_type
    )

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()
    print(f"File uploaded, type: {mime_type}, ID: {file.get("id")}")