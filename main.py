import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
REBRICKABLE_API_KEY = os.getenv('REBRICKABLE_API_KEY')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'\nBot is ready. Logged in as {bot.user.name}')


@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')



@bot.command()
async def setimage(ctx, set_number):
    try:
        headers = {'Accept': 'application/json', 'Authorization': f'key {REBRICKABLE_API_KEY}'}
        response = requests.get(f'https://rebrickable.com/api/v3/lego/sets/{set_number}/', headers=headers)
        if response.status_code == 200:
            data = response.json()
            image_url = data['set_img_url']
            await ctx.send(image_url)
        else:
            await ctx.send('Failed to fetch set information.')

    except Exception as e:
        await ctx.send(f'Error: {str(e)}')


bot.run(DISCORD_TOKEN)
