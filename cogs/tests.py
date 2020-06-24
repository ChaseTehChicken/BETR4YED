import discord
import asyncio 
from discord.ext import commands

class test(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def delete(self, ctx):
        await ctx.send('Deleting message...', delete_after=2)

def setup(client):
    client.add_cog(test(client))