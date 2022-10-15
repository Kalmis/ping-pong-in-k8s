import logging
import uuid

from fastapi import FastAPI

fmt = "%(asctime)s, %(levelname)-8s %(name)-10s [%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(encoding="utf-8", format=fmt, level=logging.INFO)
logger = logging.getLogger("log-output")

app = FastAPI()

TIMESTAMP_FILE_PATH = "/shared/timestamp.txt"
PINGPONG_FILE_PATH = "/shared/pingpong.txt"


@app.get("/")
async def root():
    with open(TIMESTAMP_FILE_PATH, "r") as f:
        timestamp = f.read()
    with open(PINGPONG_FILE_PATH, "r") as f:
        pingpong = f.read()
    return {"message": f"{timestamp} {uuid.uuid4()}\n Ping / Pongs: {pingpong}"}
