import discord
from discord.ext import commands
from discord import app_commands

import tracemalloc

INFO_CHANNEL_ID = 1451494787566796952
class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        intents = discord.Intents.all()
        self.bot = commands.Bot(command_prefix='!', intents=intents)
        self.tree = self.bot.tree

    @app_commands.command(name="info", description="En savoir plus sur la license Tomb Raider")
    async def info_command(self, interaction: discord.Interaction):

        # Vérification du salon
        if interaction.channel_id != INFO_CHANNEL_ID:
            await interaction.response.send_message(
                "Cette commande ne peut être utilisée que dans le salon #tomb-raider.",
            )
            return

        # Commande autorisée
        await interaction.response.send_message("https://www.tombraider.com")
async def setup(bot : commands.Bot):
    await bot.add_cog(Info(bot))
