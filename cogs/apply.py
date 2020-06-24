import discord
import asyncio
from discord.ext import commands

class apply(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def apply(self, ctx):
        embed1 = discord.Embed(description="Check your DM's!")
        await ctx.send(embed=embed1)
        embed2 = discord.Embed(description="Application Started!")
        await ctx.author.send(embed = embed2)
        embed3 = discord.Embed(description="What role are you looking for?")
        await ctx.author.send(embed=embed3)

def setup(client):
    client.add_cog(apply(client))