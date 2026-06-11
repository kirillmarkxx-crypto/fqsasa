import os
import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = os.getenv("API_URL")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("🤖 Bot ready\n/mine 1\n/stop 1\n/bots")


@dp.message(Command("mine"))
async def mine(msg: types.Message):
    bot_id = msg.text.split()[1]

    requests.post(f"{API_URL}/bots/{bot_id}", json={
        "command": "mine"
    })

    await msg.answer(f"⛏ Bot {bot_id} mining")


@dp.message(Command("stop"))
async def stop(msg: types.Message):
    bot_id = msg.text.split()[1]

    requests.post(f"{API_URL}/bots/{bot_id}", json={
        "command": "stop"
    })

    await msg.answer(f"🛑 Bot {bot_id} stopped")


@dp.message(Command("bots"))
async def bots_list(msg: types.Message):
    r = requests.get(f"{API_URL}/bots")
    await msg.answer(str(r.json()))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
