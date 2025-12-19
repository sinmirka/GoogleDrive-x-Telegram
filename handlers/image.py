from aiogram import Router, F
from aiogram.types import Message
from filters import is_owner
from datetime import datetime
import os

from google_drive import upload_image

router = Router()

@router.message(F.photo)
async def handle_photo(message: Message):
    if not is_owner(message=message):
        print(f"{message.from_user.username} tried to enter, access denied")
        return

    photo = message.photo[-1]
    
    filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

    await message.bot.download(
        file=photo.file_id,
        destination=filename
    )

    file_id = upload_image(filename)

    os.remove(filename)

    await message.answer("Successfully saved image")