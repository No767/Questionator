import asyncio
import logging
import os

import discord
import uvloop
from dotenv import load_dotenv

from .questionator_client import QuestionatorClient

load_dotenv()

DEV_GUILD = discord.Object(id=1033869285371691139)
QUESTIONATOR_TOKEN = os.getenv("Questionator_Dev_Token")
intents = discord.Intents.default()
intents.message_content = True

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] | %(asctime)s >> %(message)s",
    datefmt="[%m/%d/%Y] [%I:%M:%S %p %Z]",
)


async def main():
    async with QuestionatorClient(
        intents=intents, command_prefix=".", testing_guild_id=DEV_GUILD.id
    ) as bot:
        await bot.start(QUESTIONATOR_TOKEN)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())
