import discord
from discord.ext import commands
import os

secrets_dir = os.path.dir(os.path.abspath(__file__))
token_path = os.path.join(secrets_dir, 'token.txt')
with open(token_path, 'r') as token_file:
    token = token_file.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.command()
async def test(ctx, * args):
    await ctx.send('Hello World!')

client = discord.Client(intents=intents)

client.run(token)
