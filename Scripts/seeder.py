import asyncio
import logging
import os
import sys
import urllib.parse
from pathlib import Path

import uvloop
from dotenv import load_dotenv
from tortoise import Tortoise

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] | %(asctime)s [DB Seeder] >> %(message)s",
    datefmt="[%m/%d/%Y] [%I:%M:%S %p %Z]",
)
logging.getLogger("tortoise").setLevel(logging.WARNING)

path = Path(__file__).parents[0]
libsPath = os.path.join(str(path), "Bot", "Libs")
envPath = os.path.join(str(path), "Bot", ".env")
sys.path.append(libsPath)

load_dotenv(dotenv_path=envPath)

POSTGRES_USER = os.getenv("Postgres_User")
POSTGRES_PASSWORD = urllib.parse.quote_plus(os.getenv("Postgres_Password"))
POSTGRES_HOST = os.getenv("Postgres_Host")
POSTGRES_PORT = os.getenv("Postgres_Port")
POSTGRES_DB = os.getenv("Postgres_DB")
CONNECTION_URI = f"asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


async def main():
    await Tortoise.init(
        db_url=CONNECTION_URI,
        modules={"models": ["qotd.models"]},
    )
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()
    logging.info("Successfully created schemas")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())
