import logging
import asyncio

from fastapi import FastAPI

fmt = "%(asctime)s, %(levelname)-8s %(name)-10s [%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(encoding="utf-8", format=fmt, level=logging.INFO)
logger = logging.getLogger("ping-pong")

app = FastAPI()
counter_lock = asyncio.Lock()
counter = 0


@app.get("/pingpong")
async def ping_pong():
    global counter
    async with counter_lock:
        counter += 1
    return {"pong": counter}
