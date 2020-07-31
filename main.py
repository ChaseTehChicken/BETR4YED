import discord
import random
import os
import json
# import logging
import nekos
import requests
import asyncio
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix=commands.when_mentioned_or("[]"))
client.remove_command('help')
# logging.basicConfig(level=logging.INFO)
status = cycle(["[] | Sub 2 Chaseyy on yt!", "[] | OwO whats this?", "[]invite", "[]help"])

@client.event
async def on_ready():
    change_status.start()
    print(f'Successfully logged in as {client.user.name}!')
    print(f"ID = {client.user.id}")

@tasks.loop(seconds=600)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_command_error(ctx, exception):
    error = getattr(exception, "original", exception)
    if isinstance(error, discord.NotFound):
        return
    elif isinstance(exception, commands.BadArgument):
        return
    elif isinstance(exception, commands.CommandNotFound):
        return
    elif isinstance(exception, commands.MissingRequiredArgument):
        await ctx.send(f'Command is missing required argument :(')
    elif isinstance(exception, commands.MissingPermissions):
        embed = discord.Embed(description='You do not have the correct permissions to perform this command!')
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'Unhandled exception: {exception} \nPlease contact @Chaseyy for more details')

@client.command
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}') 

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzAzOTM5NDgyMDI1NzIxODc3.XqV4uw.JY8m7Us1H8NsKyQWfzmrFzrwn70')
