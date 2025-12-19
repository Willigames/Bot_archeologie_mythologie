import discord
from discord.ext import commands
from discord import app_commands
import random
import os

archeology_channel = int(os.getenv('ARCHEOLOGY_CHANNEL_ID'))

class ArcheologyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        intents = discord.Intents.all()
        self.bot = commands.Bot(command_prefix='!', intents=intents)
        self.tree = self.bot.tree

    # Afficher un site archéologique

    @app_commands.command(name="site", description="Découvrir un site archéologique célèbre")
    async def site_command(self, interaction: discord.Interaction):
         # Vérification du salon
        if interaction.channel_id != archeology_channel:
            await interaction.response.send_message(
                "Cette commande ne peut être utilisée que dans le salon #sites-archéologiques.",
            )
            return

        sites = [
            "https://www.machupicchu.gob.pe/?lang=en",
            "https://whc.unesco.org/fr/list/37",
            "https://hellenica.fr/peloponnese/mycenes/",
            "https://whc.unesco.org/fr/list/414",
            "https://www.voyagecambodge.com/guide-cambodge/destination/temples-angkor",

        ]

        # Sélectionner un site au hasard
        selected_site = random.choice(sites)
        embed = discord.Embed(title="Un artefact, un lieu ancien ou un mystère historique t’appelle. Clique sur le lien et pars explorer les secrets du passé.")
        embed.add_field(name="Lien", value=f"[Clique ici si tu veux te lancer dans l'aventure]({selected_site})")


        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(ArcheologyCog(bot))
