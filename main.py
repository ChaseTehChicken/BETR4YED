import discord
import random
import os
import json
import logging
import nekos
import requests
import asyncio
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

joinlink = 'https://bit.ly/Betr4yz'

client = commands.Bot(command_prefix= "[]")
client.remove_command('help')
logging.basicConfig(level=logging.INFO)
status = cycle(["Sub 2 Bet", f"Become a member of Bet {joinlink}", "Join bets stream some time"])

@client.event
async def on_ready():
    change_status.start()
    print(f'Successfully logged in as {client.user.name}!')
    print(f"ID = {client.user.id}")

@tasks.loop(seconds=600)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_command_error(ctx, error):
    if ctx.author.id == 420454043593342977:
        await ctx.channel.send(f"Error: {error}")
    else:
        ctx.channel.send('Theres an error here, contact @Chaseyy#9999, or a someone from the bot dev team for help')

@client.command
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}') 

#@load.error
#async def clear_error(ctx, error):
#    if isinstance(error, commands.MissingRequiredArgument):
#        await ctx.send('Command Unavaliable')


@client.event
async def on_member_join(member):
    print(f'{member} Has joined the betr4yl squad!')
    #role = discord.utils.get(ctx.guild.roles, name = "member")
    #await ctx.add_roles(role)

@client.event
async def on_member_remove(member):
    print(f'{member} has left the betr4yl squad')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('TOKEN')