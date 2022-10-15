import logging
import asyncio

from fastapi import FastAPI

fmt = "%(asctime)s, %(levelname)-8s %(name)-10s [%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(encoding="utf-8", format=fmt, level=logging.INFO)
logger = logging.getLogger("ping-pong")

app = FastAPI()
counter_lock = asyncio.Lock()

FILE_PATH = "/shared/pingpong.txt"


@app.get("/pingpong")
async def ping_pong():
    global counter
    async with counter_lock:
        # Very nice and performant async endpoint that... Locks and reads/writes a file.
        try:
            with open(FILE_PATH, "r") as f:
                counter = int(f.read())
        except FileNotFoundError:
            counter = 0
            pass
        counter += 1
        with open(FILE_PATH, "w") as f:
            f.write(str(counter))
    return {"pong": counter}
