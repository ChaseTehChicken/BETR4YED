import discord
from discord.ext import commands
import random

joinlink = 'https://bit.ly/Betr4yz'
SubLink = 'https://bit.ly/Sub2Bet'
TwitchLink = 'https://www.twitch.tv/betr4ys'
vancityTwitch = 'https://www.twitch.tv/vancityoliver'
vancityYT = 'https://bit.ly/vancityoliveryt'

#ignore change

class streams(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command()
    async def join(self, ctx):
        if ctx.guild.id == 668359349076361267:
            await ctx.send(f'Join the betr4yl squad here!: {joinlink}')
        elif ctx.guild.id == 675285751138877464:
            await ctx.send(f'You cant become a member on vancitys server, but you can become a twitch sub! {vancityTwitch}')
        else: 
            return

    @commands.command(aliases=['sub'])
    async def subscribe(self, ctx):
        if ctx.guild.id == 668359349076361267:
            await ctx.send(f'Subscribe to Bet on youtube for the ultimate flex: {SubLink}')
        elif ctx.guild.id == 675285751138877464:
            await ctx.send(f'Sub to VancityOliver on YouTube for the ultimate flex!: {vancityYT}')
        else:
            return
        
    
    @commands.command()
    async def twitch(self, ctx):
        if ctx.guild.id == 668359349076361267:
            await ctx.send(f'Follow Betr4ys on twitch!: {TwitchLink}')
        elif ctx.guild.id == 675285751138877464:
            await ctx.send(f'Follow vancityoliver on twitch!: {vancityTwitch}')
        else:
            return

    
def setup(client):
    client.add_cog(streams(client))