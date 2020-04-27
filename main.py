import discord
import random
import os
import json
import logging
import nekos
import requests
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix= "[]")
logging.basicConfig(level=logging.INFO)
status = cycle(["Sub 2 Bet", "Become a member of Bet [https://www.youtube.com/channel/UCAoQXAF7VpvjwRjvdGbX9pA/membership]", "Join bets stream some time"])

version = "0.0.1 (BETA)"
dpyVersion = discord.__version__
serverCount = len(client.guilds)
memberCount = len(set(client.get_all_members()))

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

@client.event
async def on_member_remove(member):
    print(f'{member} has left the betr4yl squad')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(manage_messages=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'successfully kicked: {member} for reason: {reason}')

@client.command
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'successfully banned: {member} for reason: {reason}')
    print(f'Member {member} banned with reason: {reason}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_descriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator) == (member_name, member_descriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Sucessfully unbanned {user}')
            print(f'Member unbanned: {member}')
            return

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('TOKEN')