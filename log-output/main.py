import logging
import uuid

from fastapi import FastAPI

fmt = "%(asctime)s, %(levelname)-8s %(name)-10s [%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(encoding="utf-8", format=fmt, level=logging.INFO)
logger = logging.getLogger("log-output")

app = FastAPI()

FILE_PATH = "/shared/timestamp.txt"


@app.get("/")
async def root():
    with open(FILE_PATH, "r") as f:
        timestamp = f.read()
    return {"message": f"{timestamp} {uuid.uuid4()}"}
