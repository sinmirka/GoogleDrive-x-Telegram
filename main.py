from config import BOT_TOKEN, OWNER_ID
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import parse_mode
from aiogram.filters import CommandStart
from aiogram.types import Message

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties())

from handlers.start import router as start_router
dp.include_router(start_router)

from handlers.text import router as text_router
dp.include_router(text_router)

from handlers.image import router as image_router
dp.include_router(image_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main=main())
    except KeyboardInterrupt:
        print("Bot turned off")