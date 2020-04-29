import discord
from discord.ext import commands
import random

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command(aliases=["8ball"])
    async def _ball(self, ctx, *, question):
        responses = ['yes',
        'maybe',
        'no']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def coinflip(self, ctx):
        HeadsTails = ['Heads',
        'Tails']
        await ctx.send(f'{random.choice(HeadsTails)}')
    
def setup(client):
    client.add_cog(fun(client))