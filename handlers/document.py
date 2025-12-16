from aiogram import Router, F
from aiogram.types import Message
from filters import is_owner
from datetime import datetime
import os

from google_drive import upload_doc

router = Router()

@router.message(F.document)
async def handle_document(message: Message):
    if not is_owner(message=message):
        print(f"{message.from_user.username} tried to enter, access denied")
        return
    
    doc = message.document
    
    filename = doc.file_name
    
    await message.bot.download(
        file=doc.file_id,
        destination=filename
    )

    upload_doc(filename, mime_type=doc.mime_type)

    os.remove(filename)

    await message.answer("Successfully saved doc file")