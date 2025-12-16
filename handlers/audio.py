from aiogram import Router, F
from aiogram.types import Message
from filters import is_owner
from datetime import datetime
import os

from google_drive import upload_video_audio

router = Router()

@router.message(F.audio)
async def handle_audio(message: Message):
    if not is_owner(message=message):
        print(f"{message.from_user.username} tried to enter, access denied")
        return
    
    audio = message.audio
    
    filename = audio.file_name
    
    await message.bot.download(
        file=audio.file_id,
        destination=filename
    )

    upload_video_audio(filename, mime_type=audio.mime_type)

    os.remove(filename)

    await message.answer(f"Successfully saved {audio.mime_type} file")