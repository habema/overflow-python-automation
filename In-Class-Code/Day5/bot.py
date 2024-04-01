# pip install -U discord.py

# Import the required modules
import discord
import os
from discord.ext import commands 
from dotenv import load_dotenv

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def greet(ctx):
    response = 'Hello, I am your discord bot'
    await ctx.send(response)


@bot.command()
async def prefix(ctx):
    global PREFIX
    PREFIX = ctx.message.content.split()[1]
    response = 'Hello, I am your discord bot'
    await ctx.send(response)

@bot.command()
async def list_command(ctx):
    response = 'You can use the following commands: \n !greet \n !list_command \n !functions'
    await ctx.send(response)

@bot.command()
async def functions(ctx):
    response = 'I am a simple Discord chatbot! I will reply to your command!'
    await ctx.send(response)

# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))