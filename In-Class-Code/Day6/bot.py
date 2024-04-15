# pip install -U discord.py

# Import the required modules
import discord
import os
from discord.ext import commands 
from dotenv import load_dotenv

import requests
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


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
async def weather(ctx):
    p = {
        'latitude': 31.95,
        'longitude': 35.91,
        'daily': ['temperature_2m_max', 'temperature_2m_min'],
        'timezone': 'auto'
    }

    r = requests.get('https://api.open-meteo.com/v1/forecast', params=p)

    df = pd.DataFrame(r.json()['daily'])

    plot = sns.lineplot(df, x = 'time', y = 'temperature_2m_max',  color='#e34040', marker = 'o')
    plot2 = sns.lineplot(df, x = 'time', y = 'temperature_2m_min',  color='#5da2f0', marker = 'o')

    plot2.set_xticklabels(plot.get_xticklabels(), rotation=45)

    plt.xlabel('Time')
    plt.ylabel('Temperature (C)')
    plt.title('Temperature in Amman')
    plt.grid()
    plt.tight_layout()
    plt.savefig('weather.png')

    await ctx.send(file=discord.File('weather.png'))


# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))