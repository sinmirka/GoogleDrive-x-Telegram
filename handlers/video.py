from aiogram import Router, F
from aiogram.types import Message
from filters import is_owner
from datetime import datetime
import os

from google_drive import upload_video_audio

router = Router()

@router.message(F.video)
async def handle_video(message: Message):
    if not is_owner(message=message):
        print(f"{message.from_user.username} tried to enter, access denied")
        return
    
    video = message.video
    
    filename = video.file_name.replace(" ", "_")
    
    await message.bot.download(
        file=video.file_id,
        destination=filename
    )

    upload_video_audio(filename, mime_type=video.mime_type)

    os.remove(filename)

    await message.answer(f"Successfully saved {video.mime_type} file")