from aiogram.types import Message
from config import OWNER_ID

def is_owner(message: Message):
    if message.from_user.id != OWNER_ID:
        print(f"{message.from_user.id} is not owner!")
        return False
    else:
        print(f"{message.from_user.id} is owner!")
        return True