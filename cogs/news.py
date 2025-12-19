import discord
from discord.ext import commands
from discord import app_commands
import os

# Récupérer l'ID du salon à partir des variables d'environnement
INFO_TOMBRAIDER_ID = int(os.getenv('INFO_TOMBRAIDER_ID'))


class NewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        intents = discord.Intents.all()
        self.bot = commands.Bot(command_prefix='!', intents=intents)
        self.tree = self.bot.tree

    # Afficher le dernier trailer de Tomb Raider
    @app_commands.command(name="trailer", description="Dernier trailer de la license Tomb Raider")
    async def trailer_command(self, interaction: discord.Interaction):

        # Vérification du salon
        if interaction.channel_id != INFO_TOMBRAIDER_ID:
            await interaction.response.send_message(
                "Cette commande ne peut être utilisée que dans le salon #tomb-raider.",
            )
            return

        # Description de la commande
        embed = discord.Embed(title="Les mystères m’attendent. Êtes-vous prêts ? Voici le dernier Tomb Raider")
        embed.set_image(url="https://gamewave.fr/static/images/news/headers/thumbs/26da3-tomb-raider-catalyst-accessible-nouveaux-venus-320x180.webp")
        embed.add_field(name="Lien", value="https://www.youtube.com/watch?v=Lc68tSz9xoc")
        await interaction.response.send_message(embed=embed)

async def setup(bot : commands.Bot):
    await bot.add_cog(NewsCog(bot))
