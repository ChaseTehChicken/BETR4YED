import discord
from discord.ext import commands
import random

joinlink = 'https://bit.ly/Betr4yz'
SubLink = 'https://bit.ly/Sub2Bet'
TwitchLink = 'https://www.twitch.tv/betr4ys'

class streams(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command()
    async def join(self, ctx):
        await ctx.send(f'Join the betr4yl squad here!: {joinlink}')

    @commands.command(aliases=['sub'])
    async def subscribe(self, ctx):
        await ctx.send(f'Subscribe to Bet on youtube for the ultimate flex: {SubLink}')
    
    @commands.command()
    async def twitch(self, ctx):
        await ctx.send(f'Follow Betr4ys on twitch!: {TwitchLink}')
    
    @commands.command()
    async def codegenerator(self, ctx):
        await ctx.send()

    
def setup(client):
    client.add_cog(streams(client))