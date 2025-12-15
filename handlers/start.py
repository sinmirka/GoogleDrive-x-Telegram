from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from filters import is_owner

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    if is_owner(message=message):
        await message.answer("Welcome, what would you like to store?")
    else:
        await message.answer("Nothing to see for ya here")