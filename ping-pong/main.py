import os
import logging

import asyncpg
from fastapi import Depends, FastAPI
from pydantic import BaseModel

fmt = "%(asctime)s, %(levelname)-8s %(name)-10s [%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(encoding="utf-8", format=fmt, level=logging.INFO)
logger = logging.getLogger("ping-pong")

app = FastAPI()

pool: asyncpg.Pool = None

# Dependency
async def get_pool() -> asyncpg.Pool:
    return pool


class Counter(BaseModel):
    pong: int


@app.on_event("startup")
async def startup_event():
    # FIXME: Use SQLAlchemy and the preferred way of handling DB connections in FastAPI
    logger.info("Starting")
    global pool
    pool = await asyncpg.create_pool(
        host="postgres-svc",
        port=5432,
        database="postgres",
        user="postgres",
        password=os.environ["POSTGRES_PASSWORD"],
    )
    async with pool.acquire() as conn:
        await conn.execute("CREATE TABLE IF NOT EXISTS counter (counter integer);")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down")
    pool.close()


@app.get("/pingpong", response_model=Counter)
async def ping_pong(pool: asyncpg.Pool = Depends(get_pool)):
    async with pool.acquire() as conn:
        await conn.execute("INSERT INTO counter VALUES (1);")
        row = await conn.fetchrow("SELECT count(*) n FROM counter;")
        logger.error(row)
        counter = row["n"]
    return Counter(pong=counter)
