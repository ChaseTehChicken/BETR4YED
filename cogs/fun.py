import discord
from discord.ext import commands
import random
import json
import random
import aiohttp
import nekos
import asyncio
import uwuify

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
    async def optout(self, ctx):
        embed = discord.Embed(
            title = f'{ctx.message.author} has opted out',
            description = f'{ctx.message.author} has opted out of the discord ToS and has been banned from the server!'
        )
        await ctx.send(embed=embed)
        await ctx.author.ban(reason='Opt out lmao')

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
    async def hug(self, ctx, member : discord.Member=None):
        hug = nekos.img('hug')
        try:
            if not member:
                embed = discord.Embed(description='Please mention a user to hug :3\nCorrect usage: []hug @user')
                await ctx.send(embed=embed, delete_after=5) 
            elif member.id == ctx.author.id:
                embed=discord.Embed(description=f'{ctx.author.name} hugs themselves! How cute :hearts:')
                embed.set_image(url=hug)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(description=f'{ctx.author.name} hugs {member.name}! How cute :hearts:')
                embed.set_image(url=hug)
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description='There was a problem with your command. Remember to specify someone to hug')
            await ctx.send(embed=embed)

    @commands.command()
    async def cuddle(self, ctx, member : discord.Member=None):
        cuddle = nekos.img('cuddle')
        try:
            if not member:
                embed = discord.Embed(description='Please mention a user to cuddle :3\nCorrect usage: []cuddle @user')
                await ctx.send(embed=embed, delete_after=5)
            elif member.id == ctx.author.id:
                embed=discord.Embed(description=f'{ctx.author.name} cuddles themself. How cuute :hearts:')
                embed.set_image(url=cuddle)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(description=f'{ctx.author.name} cuddles {member.name}! How cute :hearts:')
                embed.set_image(url=cuddle)
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description='There was a problem with your command. Specify a member to cuddle, and try again')
            await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member : discord.Member=None):
        kissgif = nekos.img('kiss')
        try:
            if not member:
                embed = discord.Embed(description='Please mention a user to kiss :3\nCorrect usage: []kiss @user')
                await ctx.send(embed=embed, delete_after=5)
            elif member.id == ctx.author.id:
                embed = discord.Embed(description=f'{ctx.author.name} kisses them self, how cute :hearts:')
                embed.set_image(url=kissgif)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'{ctx.author.name} kisses {member.name}! How cute :hearts:')
                embed.set_image(url=kissgif)
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description='There was a problem with your command. Specify a member to kiss, and try again')
            await ctx.send(embed=embed)

    @commands.command()
    async def poke(self, ctx, member : discord.Member=None):
        poke = nekos.img('poke')
        try:
            if not member:
                embed = discord.Embed(description='Please mention a user to poke :3\nCorrect usage: []poke @user')
                await ctx.send(embed=embed, delete_after=5)
            elif member.id == ctx.author.id:
                embed = discord.Embed(description=f'{ctx.author.name} pokes themself.. weird.. :hearts:')
                embed.set_image(url=poke)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'{ctx.author.name} pokes {member.name}... :hearts:')
                embed.set_image(url=poke)
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description='There was a problem with your command. Specify a member to poke, and try again')

    # @commands.command()
    # async def ghost(self, ctx, member : discord.Member=None, amount=5):
    #     try:
    #         if ctx.author.id != 420454043593342977:
    #             if not member:
    #                 embed = discord.Embed(description="Please specify a server member to ping!")
    #                 await ctx.send(embed=embed)
    #             elif amount <= 5:
    #                 embed = discord.Embed(description='Please choose a number between 5 and 20')
    #                 await ctx.send(embed=embed)
    #             elif amount > 20:
    #                 embed = discord.Embed(description="This bot cannot ghost ping people more than 20 times")
    #                 await ctx.send(embed=embed)
    #             else:
    #                 msg = ctx.message
    #                 await msg.delete()
    #                 for i in range(1, amount+1):
    #                     await ctx.send(f'<@{member.id}>', delete_after=1)
    #         else:
    #             if not member:
    #                 embed = discord.Embed(description="Please specify a server member to ping!")
    #                 await ctx.send(embed=embed)
    #             elif amount <= 5:
    #                 embed = discord.Embed(description='Please choose a number between 5 and 20')
    #                 await ctx.send(embed=embed)
    #             else:
    #                 msg = ctx.message
    #                 await msg.delete()
    #                 for i in range(1, amount+1):
    #                     await ctx.send(f'<@{member.id}>', delete_after=1)
    #     except Exception as e:
    #         embed = discord.Embed(description='Sorry, we seem to have ran into an error. Remember to specify a member to ping, if the problem persists, contact Chaseyy#9999 for more info')
    #         await ctx.send(embed=embed)

    @commands.command()
    async def gaymeter(self, ctx, member : discord.Member=None):
        try:
            if not member:
                embed = discord.Embed(description=f'{ctx.author.name}, you are {random.randint(0,101)}% gay\n:rainbow_flag:')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'{member.name} is {random.randint(0,101)}% gay\n:rainbow_flag:')
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description=f'We have ran into an error. Error code: {e}\nContact Chaseyy#9999 for support')
            await ctx.send(embed=embed)
    
    @commands.command()
    async def epicgamerrate(self, ctx, member : discord.Member=None):
        try:
            if not member:
                embed = discord.Embed(description=f'{ctx.author.name}, you are {random.randint(1,101)}% Epic')
                await ctx.send(embed=embed)
            elif member.id == ctx.author.id:
                embed = discord.Embed(description=f'{ctx.author.name}, you are {random.randint(1,101)}% Epic')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'{member.name}, you are {random.randint(1,101)}% Epic')
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description=f'We have ran into an error. Error code: {e}\nContact Chaseyy#9999 for support')

    @commands.command()
    async def simpmeter(self, ctx, member : discord.Member=None):
        try:
            if not member:
                embed = discord.Embed(description=f'{ctx.author.name} is {random.randint(0, 101)}% simp')
                await ctx.send(embed=embed)
            elif member.id == ctx.author.id:
                embed = discord.Embed(description=f'{ctx.author.name} is {random.randint(0, 101)}% simp')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'{member.name} is {random.randint(0, 101)}% simp')
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description=f'We have ran into an error. Error code: {e}\nContact Chaseyy#9999 for support')
            await ctx.send(embed=embed)

    @commands.command()
    async def clap(self, ctx, *, args):
        try:
            if not ' ' in args:
                charList = [char for char in args]
                sendText = ' '.join(map(str, charList))
                await ctx.send(sendText.replace(' ', ' :clap: '))
                return
            await ctx.send(args.replace(' ', ' :clap: '))
        except Exception as e:
            embed = discord.Embed(description=f'We have ran into an error (probably out of hands to clap with). Error code: {e}\nContact Chaseyy#9999 for support')
            await ctx.send(embed=embed)

    @commands.command()
    async def google(self, ctx, *, args):
        try:
            if not ' ' in args:
                await ctx.send(f'<http://lmgtfy.com/?q={args}&pp=1>')
                return
            await ctx.send(f"<http://lmgtfy.com/?q={args.replace(' ', '+')}&pp=1>")
        except Exception as e:
            embed = discord.Embed(description=f'That question was too hard to google.. Error code: {e}\nContact Chaseyy#999 for support')
            await ctx.send(embed=embed)

    @commands.command()
    async def uwuify(self, ctx, *, args):
        flags = uwuify.SMILEY | uwuify.YU
        await ctx.send(uwuify.uwu(args, flags=flags))
    
    @commands.command()
    async def # finishing soon


def setup(client):
    client.add_cog(fun(client))
