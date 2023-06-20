import discord
from discord.ext import commands
import os

secrets_dir = os.path.dir(os.path.abspath(__file__))
token_path = os.path.join(secrets_dir, 'token.txt')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.command()
async def test(ctx):
    pass

client = discord.Client(intents=intents)

client.run('e')
