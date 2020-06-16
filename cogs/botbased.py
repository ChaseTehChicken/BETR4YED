import discord
from discord.ext import commands

version = "0.1.7"
dpyVersion = discord.__version__
serverCount = 2
memberCount = 0

class BotBased(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def stats(self, ctx):
        embed = discord.Embed( 
            title=f'{self.client.user.name} Stats',  
            description="\uFEFF", 
            colour=ctx.author.colour, 
            timestamp=ctx.message.created_at) 
        embed.add_field(name='Bot Version:', value=version)
        embed.add_field(name='Discord.Py Version', value=dpyVersion)
        embed.add_field(name='Total Guilds:', value=serverCount)
        embed.add_field(name='Total Users:', value=memberCount)
        embed.add_field(name='Bot Developers:', value="<@420454043593342977>")
        embed.set_footer(text=f"Carpe Noctem | {self.client.user.name}")
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
        print(f'{ctx.author.name} used command Stats')

def setup(client):
    client.add_cog(BotBased(client))