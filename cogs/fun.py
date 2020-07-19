import discord
from discord.ext import commands
import random
import json
import random
import aiohttp
import nekos
import asyncio

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command(aliases=["8ball"])
    async def _ball(self, ctx, *, question):
        try:
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
        except Exception as e:
            embed = discord.Embed(description='Please ask a question for the 8ball\n\nCorrect usage: []8ball [question]')
            await ctx.send(embed=embed)

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
        try:
            if not member:
                embed = discord.Embed(description='Please specify a member to beat the shit out of')
                await ctx.send(embed=embed)
            
            if member.id == ctx.author.id:
                embed = discord.Embed(
                    title=f'{ctx.author.name} slapped themselves! Ouch..'

                )
                embed.set_image(url=slap)
                await ctx.send(embed=embed)
            else:
                slap = nekos.img('slap')
                embed = discord.Embed(title=f'{ctx.author.name} slapped {member.name}! Ouch!')
                embed.set_image(url=slap)
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description='We\'ve run into an error. Please make sure you specify a member to slap')
            await ctx.send(embed=embed)

    @commands.command()
    async def ghost(self, ctx, member : discord.Member=None, amount=5):
        try:
            if ctx.author.id != 420454043593342977:
                if not member:
                    embed = discord.Embed(description="Please specify a server member to ping!")
                    await ctx.send(embed=embed)
                elif amount <= 5:
                    embed = discord.Embed(description='Please choose a number between 5 and 20')
                    await ctx.send(embed=embed)
                elif amount > 20:
                    embed = discord.Embed(description="This bot cannot ghost ping people more than 20 times")
                    await ctx.send(embed=embed)
                else:
                    msg = ctx.message
                    await msg.delete()
                    for i in range(1, amount+1):
                        await ctx.send(f'<@{member.id}>', delete_after=1)
            else:
                if not member:
                    embed = discord.Embed(description="Please specify a server member to ping!")
                    await ctx.send(embed=embed)
                elif amount <= 5:
                    embed = discord.Embed(description='Please choose a number between 5 and 20')
                    await ctx.send(embed=embed)
                else:
                    msg = ctx.message
                    await msg.delete()
                    for i in range(1, amount+1):
                        await ctx.send(f'<@{member.id}>', delete_after=1)
        except Exception as e:
            embed = discord.Embed(description='Sorry, we seem to have ran into an error. Remember to specify a member to ping, if the problem persists, contact Chaseyy#9999 for more info')
            await ctx.send(embed=embed)

    #@ghost.error()
    #async def ghost_error(self, ctx, error):
    #    if isinstance(error, (ConversionError, BadArgument)):
    #        await ctx.send('Member not found!')
    #    else:
    #        raise error


def setup(client):
    client.add_cog(fun(client))