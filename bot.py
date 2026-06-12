import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import redis

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Привет! Отправь мне сообщение, и я сохраню его в Redis."
    )


@dp.message()
async def save_message(message: Message):

    username = (
        message.from_user.username
        if message.from_user.username
        else str(message.from_user.id)
    )

    redis_client.rpush(
        "messages",
        f"{username}: {message.text}"
    )

    await message.answer(
        "Сообщение сохранено в Redis ✅"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())