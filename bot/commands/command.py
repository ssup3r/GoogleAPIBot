import discord
from discord import app_commands
import bot_main

intents = bot_main.intents
client = bot_main.client
tree = app_commands.CommandTree(client)

@tree.command(name = "Get assignments from all classes", description = "Retreive all available assignments from all classes", guild=discord.Object(id=1))
async def getassignmentall(interaction):
    pass