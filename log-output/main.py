import logging
import os
import uuid

import aiohttp
from fastapi import FastAPI

fmt = "%(asctime)s, %(levelname)-8s %(name)-10s [%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(encoding="utf-8", format=fmt, level=logging.INFO)
logger = logging.getLogger("log-output")

app = FastAPI()

TIMESTAMP_FILE_PATH = "/shared/timestamp.txt"
PINGPONG_URL = "http://ping-pong-svc"


@app.get("/")
async def root():
    with open(TIMESTAMP_FILE_PATH, "r") as f:
        timestamp = f.read()
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{PINGPONG_URL}/pingpong") as resp:
            data = await resp.json()
    return {
        "message": f"{os.environ.get('MESSAGE', 'Env not set')} {timestamp} {uuid.uuid4()}\n Ping / Pongs: {data.get('pong', None)}"
    }
