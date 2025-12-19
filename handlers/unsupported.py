from aiogram import Router
from aiogram.types import Message
from filters import is_owner

router = Router()

@router.message()
async def handle_unsupported(message: Message):
    if not is_owner(message):
        return

    await message.answer(
        "This file type is currently unsupported."
    )