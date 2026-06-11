from fastapi import FastAPI
from db import bots

app = FastAPI()

# получить команду для бота
@app.get("/bots/{bot_id}")
def get_bot(bot_id: str):
    return bots.get(bot_id, {"command": "idle"})


# установить команду (из Telegram)
@app.post("/bots/{bot_id}")
def set_bot(bot_id: str, data: dict):
    bots[bot_id] = data
    return {"ok": True}


# статус всех ботов
@app.get("/bots")
def all_bots():
    return bots
