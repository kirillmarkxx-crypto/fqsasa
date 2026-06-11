from fastapi import FastAPI

app = FastAPI()

bots = {str(i): {"command": "idle"} for i in range(1, 9)}


@app.get("/bots")
def all_bots():
    return bots


@app.get("/bots/{bot_id}")
def get_bot(bot_id: str):
    return bots.get(bot_id, {"command": "idle"})


@app.post("/bots/{bot_id}")
def set_bot(bot_id: str, data: dict):
    bots[bot_id] = data
    return {"ok": True}
