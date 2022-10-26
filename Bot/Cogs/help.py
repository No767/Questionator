import discord
from discord import app_commands
from discord.ext import commands


class HelpSelect(discord.ui.Select):
    def __init__(self, bot) -> None:
        self.bot = bot
        options = [
            discord.SelectOption(label=cog_name, description=cog.__doc__)
            for cog_name, cog in sorted(bot.cogs.items())
        ]
        super().__init__(
            placeholder="Select a command",
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("This is a test command!")


class Help(commands.Cog):
    """Commands for getting commands and their info for Questionator"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="The help page for Questionator")
    async def questionatorHelp(self, interaction: discord.Interaction):
        """The help page for Questionator
        Args:
            interaction (discord.Interaction): Interaction to respond to
        """
        embed = discord.Embed()
        embed.title = self.bot.user.name
        embed.description = f"{self.bot.user.name} is a QOTD bot meant a special discord server.\nUse the menu below to view commands"
        embed.add_field(name="Server Count", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="User Count", value=len(self.bot.users), inline=True)
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        view = discord.ui.View().add_item(HelpSelect(self.bot))
        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Help(bot))
