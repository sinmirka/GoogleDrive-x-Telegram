from aiogram import Router, F
from aiogram.types import Message
from filters import is_owner
from datetime import datetime
import os

from google_drive import upload_voice

router = Router()

@router.message(F.voice)
async def handle_voice(message: Message):
    if not is_owner(message=message):
        print(f"{message.from_user.username} tried to enter, access denied")
        return
    
    voice = message.voice
    try:
        filename = f"voice_{message.forward_sender_name.replace(" ", "_")}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.ogg"
    except Exception:
        filename = f"voice_{message.from_user.username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.ogg"

    await message.bot.download(
        file=voice.file_id,
        destination=filename
    )

    upload_voice(filename, mime_type=voice.mime_type)

    os.remove(filename)

    await message.answer("Successfully saved voice message")