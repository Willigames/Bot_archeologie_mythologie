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



@bot.event
async def on_ready():
    await bot.load_extension("cogs.news")
    await bot.load_extension("cogs.journey")
    await bot.load_extension("cogs.archeology_sites")
    await bot.load_extension("cogs.infos_tomb_raider")
    await bot.tree.sync()
    print("Bot lancé")






bot.run(os.getenv('DISCORD_TOKEN'))