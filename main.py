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
    print(f'Bot is ready. Logged in as {bot.user.name}')


@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')



@bot.command()
async def setimage(ctx, set_number):
    try:
        # Make a GET request to the Rebrickable API to get set information
        headers = {'Accept': 'application/json', 'Authorization': f'key {REBRICKABLE_API_KEY}'}
        response = requests.get(f'https://rebrickable.com/api/v3/lego/sets/{set_number}/', headers=headers)
        if response.status_code == 200:
            data = response.json()

            # Extract the image URL from the response
            image_url = data['set_img_url']

            # Send the image as a response
            await ctx.send(image_url)
        else:
            await ctx.send('Failed to fetch set information.')

    except Exception as e:
        await ctx.send(f'Error: {str(e)}')


bot.run(DISCORD_TOKEN)
