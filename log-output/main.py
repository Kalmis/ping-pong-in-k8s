import logging
import uuid

from fastapi import FastAPI

fmt = "%(asctime)s, %(levelname)-8s %(name)-10s [%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(encoding="utf-8", format=fmt, level=logging.INFO)
logger = logging.getLogger("log-output")

app = FastAPI()

RANDOM_STRING = uuid.uuid4()


@app.get("/")
async def root():
    return {"message": f"{RANDOM_STRING} {uuid.uuid4()}"}
