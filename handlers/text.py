from aiogram import Router, F
from aiogram.types import Message
from filters import is_owner
from datetime import datetime
import os

from google_drive import upload_txt

router = Router()

@router.message(F.text)
async def handle_text(message: Message):
    if not is_owner(message=message):
        print(f"{message.from_user.username} tried to enter, access denied")
        return
    
    filename = f"text_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    text = str(message.text + " --- " + message.from_user.username)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    
    file_id = upload_txt(filename)

    os.remove(filename)

    await message.answer("Successfully saved text file")