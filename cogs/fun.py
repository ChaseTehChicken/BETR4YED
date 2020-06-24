import discord
from discord.ext import commands
import random
import json
import random
import aiohttp
import nekos

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
    
    @commands.command()
    async def optout(self, ctx):
        embed = discord.Embed(
            title = f'{ctx.message.author} has opted out',
            description = f'{ctx.message.author} has opted out of the discord ToS and has been banned from the server!'
        )
        await ctx.send(embed=embed)
        await ctx.author.ban(reason='Opt out lmao')
    
    #@commands.command()
    #async def kill(self, ctx, member : discord.Member):
    #   deaths = [f'{ctx.message.author} stabs {member}.. get deaded', f'{member} mysteriously disappears from earth...', f'{member} gets crushed by a mysterious boulder..']
    #   await ctx.send(random.choice(deaths))

    @commands.command()
    async def rr(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    @commands.command()
    async def slap(self, ctx, *, member : discord.Member):
        
        slap = nekos.img('slap')
        if member.id == ctx.author.id:
            embed = discord.Embed(
                title=f'{ctx.author.name} slapped themselves! Ouch..'
                
            )
            embed.set_image(url=slap)
            await ctx.send(embed=embed)
        else:
            slap = nekos.img('slap')
            embed = discord.Embed(title=f'{ctx.author.name} slapped {member.nick}! Ouch!')
            embed.set_image(url=slap)
            await ctx.send(embed=embed)
def setup(client):
    client.add_cog(fun(client))