import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Loading Token from .env file
load_dotenv()
token = os.getenv("TOKEN")

# Setting basic intents 
intents = discord.Intents.default()
intents.message_content= True
intents.members= True
intents.presences= True

# here I created the bot object with the prefix and intents that i set up above
bot = commands.Bot(command_prefix=",", intents=intents)

# here I defined a function `on_ready` 
# async means function can pause and wait, and its used to talk to discord's api
# bot.event this is called a `decorator`, it just tells the bot to run this function when this `on_ready` event happens

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def setup_hook():
    await bot.load_extension("cogs.utility")
    await bot.load_extension("cogs.errors")

bot.setup_hook = setup_hook

bot.run(token)