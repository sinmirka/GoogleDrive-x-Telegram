from aiogram import Router, F
from aiogram.types import Message
from filters import is_owner
from datetime import datetime
import os

from google_drive import upload_video_audio

router = Router()

@router.message(F.video_note)
async def handle_video_note(message: Message):
    if not is_owner(message=message):
        print(f"{message.from_user.username} tried to enter, access denied")
        return
    
    video_note = message.video_note
    
    try:
        filename = f"video_note_{message.forward_sender_name.replace(" ", "_")}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    except Exception:
        filename = f"video_note_{message.from_user.username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    
    await message.bot.download(
        file=video_note.file_id,
        destination=filename
    )

    upload_video_audio(filename, mime_type="video/mp4")

    os.remove(filename)

    await message.answer("Successfully saved video/mp4 file")