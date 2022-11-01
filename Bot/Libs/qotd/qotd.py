import asyncio
from datetime import datetime

import uvloop
from tortoise import Tortoise
from tortoise.queryset import QuerySetSingle

from . import QGuilds, Question


class QuestionatorQOTDUtils:
    """Questionator's custom QOTD utilities"""

    def __init__(self, uri: str, models: list):
        """Constructor for the QuestionatorQOTDUtils class.

        Args:
            uri (str): The connection URI for the database.
            models (list): A list of models to be used.
        """
        self.self = self
        self.uri = uri
        self.models = models

    async def addGuild(self, guild_id: int, date_added: datetime) -> None:
        """Adds a guild to the DB

        Args:
            guild_id (int): Discord Guild ID
            date_added (datetime): The datetime that they were added in
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        await QGuilds.create(id=guild_id, date_added=date_added)
        await Tortoise.close_connections()

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def addQuestion(
        self,
        guild_id: int,
        author_id: int,
        name: str,
        question: str,
        date_added: datetime,
        author_name: str,
    ) -> None:
        """Adds a question to the DB

        Args:
            guild_id (int): Discord Guild ID
            author_id (int): Discord User ID
            name (str): The name of the question to add
            question (str): The question
            date_added (datetime): The datetime that they were added in
            author_name (str): The name of the author
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        await Question.create(
            guild_id=guild_id,
            author_id=author_id,
            name=name,
            question=question,
            date_added=date_added,
            author_name=author_name,
        )
        await Tortoise.close_connections()

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def getAllQuestions(self, guild_id: int) -> list:
        """Gets all of the questions that the guild has stored

        Args:
            guild_id (int): Discord Guild ID

        Returns:
            list: A `list` containing any data needed
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        returnData = await Question.filter(guild_id=guild_id).all().values()
        await Tortoise.close_connections()
        return returnData

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def getAllOwnerQuestions(self, guild_id: int, author_id: int) -> list:
        """Obtains all of the owner's questions

        Args:
            guild_id (int): Discord Guild ID
            author_id (int): Discord User ID

        Returns:
            list: A `list` containing any data needed
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        returnData = (
            await Question.filter(guild_id=guild_id, author_id=author_id).all().values()
        )
        await Tortoise.close_connections()
        return returnData

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def getOneOwnerQuestion(
        self, guild_id: int, author_id: int
    ) -> QuerySetSingle:
        """Just gets one question for the owner

        Args:
            guild_id (int): Discord Guild ID
            author_id (int): Discord User ID

        Returns:
            QuerySetSingle: Returns an object of `tortoise.queryset.QuerySet`
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        returnData = await Question.filter(
            guild_id=guild_id, author_id=author_id
        ).first()
        await Tortoise.close_connections()
        return returnData

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
