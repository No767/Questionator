import platform

import discord
from discord import app_commands
from discord.ext import commands


class Info(commands.Cog):
    """Commands to get info about the bot and basic info commands"""

    def __init__(self, bot):
        self.bot = bot

    info = app_commands.Group(
        name="info", description="Info about Questionator and users"
    )

    @info.command(name="bot")
    async def botInfo(self, interaction: discord.Interaction):
        """Returns any info about Questionator

        Args:
            interaction (discord.Interaction): Base interaction
        """
        embed = discord.Embed()
        embed.title = f"{self.bot.user.name} Info"
        embed.add_field(name="Server Count", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="User Count", value=len(self.bot.users), inline=True)
        embed.add_field(
            name="Ping", value=f"{self.bot.latency * 1000:.2f}ms", inline=True
        )
        embed.add_field(
            name="Python Version", value=platform.python_version(), inline=True
        )
        embed.add_field(
            name="Discord.py Version", value=discord.__version__, inline=True
        )
        embed.set_footer(text=f"Made by No767")
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Info(bot))
