import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

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


bot.run(DISCORD_TOKEN)
