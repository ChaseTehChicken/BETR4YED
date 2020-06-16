import discord
from discord.ext import commands
import random
import json

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command(aliases=["8ball"])
    async def _ball(self, ctx, *, question):
        if question == 'yes':
            responses = ['yes']
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
        else:
            responses = ['yes',
            'maybe',
            'no',
            'idk, maybe?',
            'What kind of stupid question is that',
            'No chance bud']
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def coinflip(self, ctx):
        HeadsTails = ['Heads',
        'Tails']
        await ctx.send(f'{random.choice(HeadsTails)}')
    
    @commands.command()
    async def kill(self, ctx, member : discord.Member):
        await ctx.send(f'you stabbed {member}.... good job :+1:')
    
def setup(client):
    client.add_cog(fun(client))