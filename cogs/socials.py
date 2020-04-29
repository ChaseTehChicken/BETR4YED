import discord
from discord.ext import commands


InstagramLink = 'https://www.instagram.com/bet.yt/'
Discord = 'https://discord.gg/9VP9JCP'
TwitterLink = 'https://twitter.com/Betr4ys'
SubLink = 'https://bit.ly/Sub2Bet'

class social(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(aliases=['code'])
    async def creatorcode(self, ctx):
        await ctx.send('Use code Betr4yz in the fortnite item shop for the ultimate flex, and a shoutout on Bet\'s instagram')
    @commands.command(aliases=['insta'])
    async def instagram(self, ctx):
        await ctx.send('yes')
    @commands.command()
    async def epic(self, ctx):
        await ctx.send('Send Bet an epic games friend request!: Betr4yz')
    @commands.command()
    async def psn(self, ctx):
        await ctx.send('Send Bet a PSN Friend request!: Betr4yz_yt')
    @commands.command()
    async def twitter(self, ctx):
        await ctx.send(f'Follow Bet on twitter!: {TwitterLink}')
    @commands.command(aliases=['yt'])
    async def youtube(self, ctx):
        await ctx.send(f'Subscribe to Bet on YouTube!: {SubLink}')
    
def setup(client):
    client.add_cog(social(client))