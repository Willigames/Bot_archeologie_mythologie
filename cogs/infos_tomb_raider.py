import discord
from discord.ext import commands
from discord import app_commands
import os

# Récupérer l'ID du salon à partir des variables d'environnement
INFO_TOMBRAIDER_ID = int(os.getenv('INFO_TOMBRAIDER_ID'))


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        intents = discord.Intents.all()
        self.bot = commands.Bot(command_prefix='!', intents=intents)
        self.tree = self.bot.tree

    # Afficher des informations sur Tomb Raider
    @app_commands.command(name="info", description="En savoir plus sur la license Tomb Raider")
    async def info_command(self, interaction: discord.Interaction):

        # Vérification du salon
        if interaction.channel_id != INFO_TOMBRAIDER_ID:
            await interaction.response.send_message(
                "Cette commande ne peut être utilisée que dans le salon #tomb-raider.",
            )
            return

        # Commande autorisée
        embed = discord.Embed(title="Clique ici pour en savoir plus sur Tomb Raider")
        embed.url = "https://www.tombraider.com"
        embed.set_image(url="https://tse4.mm.bing.net/th/id/OIP.nQ7kjETgRuicgljrnBk4gQHaEo?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3")
        await interaction.response.send_message(embed=embed)

async def setup(bot : commands.Bot):
    await bot.add_cog(Info(bot))
