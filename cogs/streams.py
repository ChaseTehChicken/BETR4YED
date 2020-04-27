import discord
from discord.ext import commands
import random

joinlink = 'https://bit.ly/betr4yz'
SubLink = 'https://bit.ly/Sub2Bet'
TwitchLink = 'https://www.twitch.tv/betr4ys'

class joinn(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command()
    async def join(self, ctx):
        await ctx.send(f'Join the betr4yl squad here!: {joinlink}')

    @commands.command(aliases=['sub'])
    async def subscribe(self, ctx):
        await ctx.send(f'Subscribe to Bet on youtube for the ultimate flex: {SubLink}')
    
def setup(client):
    client.add_cog(joinn(client))