import asyncio
import logging
import os
from pathlib import Path
from typing import Optional

import discord
import uvloop
from discord.ext import commands
from dotenv import load_dotenv


class QuestionatorClient(commands.Bot):
    def __init__(
        self,
        *,
        intents: discord.Intents,
        command_prefix: Optional[str] = ".",
        testing_guild_id: Optional[int] = None,
    ):
        super().__init__(intents=intents, command_prefix=command_prefix)
        self.testing_guild_id = testing_guild_id

    async def on_ready(self):
        logging.info(f"Logged in as {self.user.name}")
        logging.info(
            f"{self.user.name} is ready to go! All checkers are loaded and ready!"
        )
        await self.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="/help")
        )

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def setup_hook(self):
        path = Path(__file__).parents[0]
        cogsPath = os.path.join(path, "Cogs")
        for cog in os.listdir(cogsPath):
            if cog.endswith(".py"):
                await self.load_extension(f"Cogs.{cog[:-3]}")
        if self.testing_guild_id:
            guild = discord.Object(self.testing_guild_id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


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
