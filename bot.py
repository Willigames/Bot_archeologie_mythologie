import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv() # Charger les variables d'environnement à partir du fichier .env
import os


print("Lara Croft est prête pour l'aventure!")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
tree = bot.tree

@bot.tree.command(name="info", description="En savoir plus sur la license Tomb Raider")
async def info_command(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.tombraider.com/")


@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot lancé")





bot.run(os.getenv('DISCORD_TOKEN'))