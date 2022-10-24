import discord
from discord import app_commands
from discord.ext import commands


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="test", description="Another testing command")
    async def test(self, interaction: discord.Interaction):
        """Testing command

        Args:
            interaction (discord.Interaction): The interaction to respond to
        """
        await interaction.response.send_message("This is a test command!")


async def setup(bot):
    await bot.add_cog(test(bot))
