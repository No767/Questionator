import discord
from discord import app_commands
from discord.ext import commands


class QuestionOfTheDay(commands.Cog):
    """Commands for Questionator's QOTD feature"""

    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    qotd = app_commands.Group(
        name="qotd", description="Commands for interacting with QOTD"
    )

    @qotd.command(name="add")
    async def addQuestion(self, interaction: discord.Interaction):
        """Add a question to be used in the QOTD

        Args:
            interaction (discord.Interaction): Base Interaction
        """
        await interaction.response.send_message("This command is not yet implemented")


async def setup(bot):
    await bot.add_cog(QuestionOfTheDay(bot))
