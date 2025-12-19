import discord
from discord.ext import commands
from discord import app_commands
import os

# Récupérer l'ID du salon à partir des variables d'environnement
INFO_TOMBRAIDER_ID = int(os.getenv('INFO_TOMBRAIDER_ID'))

# Classe de gestion des expéditions
class JourneyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        intents = discord.Intents.all()
        self.bot = commands.Bot(command_prefix='!', intents=intents)
        self.tree = self.bot.tree

    # Commande de liste des expéditions
    @app_commands.command(name="journey", description="Liste de mes expeditions les plus populaires")
    async def list_expeditions(self, interaction: discord.Interaction):
        if interaction.channel_id != INFO_TOMBRAIDER_ID:
            await interaction.response.send_message(
                "Cette commande ne peut être utilisée que dans le salon #tomb-raider.",
            )
            return
        """Liste les expéditions archéologiques disponibles"""
        
        expeditions = [
            {
                "titre": "L'Atlentide : Le commencement de ma légende",
                "description": "C’est ici que tout a commencé : j’ai affronté des ruines antiques, des pièges mortels et des créatures oubliées pour découvrir les secrets du Scion… et prouver que je n’étais pas simplement une aristocrate curieuse"
            },
            {
                "titre": "A la recherche de Mjolnir",
                "description": "Je suis partie à la recherche du puissant Mjolnir, explorant des sanctuaires nordiques gelés et défiant mes ennemis les plus dangereux, tout en découvrant des légendes plus anciennes que le temps lui‑même"
            },
            {
                "titre": "l’île de Yamatai",
                "description": "Perdue avec mon équipage sur l’île maudite de Yamatai, j’ai survécu contre toute attente… et j’ai commencé à forger la survivante que je suis aujourd’hui."
            },
            {
                "titre": "la cité de Kitezh",
                "description": "Encore hantée par mon passé, j’ai plongé dans la neige de la Sibérie à la quête de la cité légendaire de Kitezh, déterminée à révéler des mystères plus vastes que ma propre histoire."
            },
            {
                "titre": "L’Héritage des Dieux Mayas",
                "description": "Quand mes actions ont déclenché une apocalypse maya, je n’ai pas fui… j’ai plongé en pleine jungle, contre Trinity et contre le destin lui‑même, pour sauver le monde que je chéris."
            }
        ]

        embed = discord.Embed(
            title="🏛️ Voici quelque une des expéditions qui m'ont marquées. ",
            color=discord.Color.gold()
        )

        for expedition in expeditions:
            embed.add_field(
                name=expedition["titre"],
                value=expedition["description"],
                inline=False
            )
        
        # Envoi de l'embed
        await interaction.response.send_message(embed=embed)

async def setup(bot : commands.Bot):
    await bot.add_cog(JourneyCog(bot))