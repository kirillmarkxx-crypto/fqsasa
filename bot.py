import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import BOT_TOKEN

API_URL = "http://127.0.0.1:8080"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer(
        "🤖 Anarchy Control\n\n"
        "/bots - список\n"
        "/mine <id> - копать\n"
        "/stop <id> - стоп\n"
        "/status - статус"
    )


@dp.message(Command("bots"))
async def bots_list(msg: types.Message):
    r = requests.get(f"{API_URL}/bots")
    await msg.answer(f"📊 Bots:\n{r.text}")


@dp.message(Command("mine"))
async def mine(msg: types.Message):
    bot_id = msg.text.split()[1]

    requests.post(f"{API_URL}/bots/{bot_id}", json={
        "command": "mine"
    })

    await msg.answer(f"⛏ Bot {bot_id} mining started")


@dp.message(Command("stop"))
async def stop(msg: types.Message):
    bot_id = msg.text.split()[1]

    requests.post(f"{API_URL}/bots/{bot_id}", json={
        "command": "stop"
    })

    await msg.answer(f"🛑 Bot {bot_id} stopped")


@dp.message(Command("status"))
async def status(msg: types.Message):
    r = requests.get(f"{API_URL}/bots")
    await msg.answer(r.text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
