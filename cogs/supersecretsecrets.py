######################################################################################
# No. Before you ask, there is nothing malicous here. Even though I am the only user #
# who can use these commands, they are just bot stats, and fun commands.             #
# Im not dumb, im just stupid. Im not using haxorz to get control of peoples servers #
######################################################################################
import discord
from discord.ext import commands

class supersecretsecrets(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=[""])
    async def servercount(self, ctx):
        if ctx.message.author.id == 420454043593342977 or 442313110343254016:
            await ctx.send("I'm in " + str(len(self.client.guilds)) + " servers")
        else:
            await ctx.send('You do not have permission to use this command!')

    @commands.command()
    async def fuckyou(self, ctx, member : discord.Member):
        if ctx.message.author.id == 420454043593342977:
            await ctx.send(f'Go fuck yourself {member}')
        else:
            await ctx.send('You do not have permission to use this command!')

def setup(client):
    client.add_cog(supersecretsecrets(client))