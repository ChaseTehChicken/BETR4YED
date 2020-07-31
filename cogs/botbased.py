import discord
from discord.ext import commands

version = "2.0.1"
dpyVersion = discord.__version__

class BotBased(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def stats(self, ctx):
        serverCountrrr = str(len(self.client.guilds))
        ping = round(self.client.latency * 1000)
        servers = self.client.guilds
        sum = 0
        for s in servers:
            sum += len(s.members)
        embed = discord.Embed( 
            title=f'{self.client.user.name} Stats',  
            description="\uFEFF", 
            colour=ctx.author.colour, 
            timestamp=ctx.message.created_at) 
        embed.add_field(name='Bot Version:', value=version)
        embed.add_field(name='Discord.Py Version', value=dpyVersion)
        embed.add_field(name='Total Guilds:', value=serverCountrrr)
        embed.add_field(name='Serving:', value=f'{sum} members!')
        embed.add_field(name='Ping to API:', value=ping)
        embed.add_field(name='Bot Developers:', value="<@420454043593342977>")
        embed.set_footer(text=f"Carpe Noctem | {self.client.user.name}")
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['source'])
    async def github(self, ctx):
        embed = discord.Embed(description='[View the source code for JASON (Formerly BETR4YED) here :)](https://github.com/ChaseTehChicken/BETR4YED)')
        await ctx.send(embed=embed)
    
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(description='[Add this epic gamer bot to your server](https://discordapp.com/oauth2/authorize?client_id=703939482025721877&scope=bot&permissions=2146958847)')
        await ctx.send(embed=embed)
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms', delete_after=5)
    
    @commands.command()
    async def serving(self, ctx):
        servers = self.client.guilds
        sum = 0
        for s in servers:
            sum += len(s.members)
        
        await ctx.send(f'Serving {sum} members!')

    @commands.command()
    async def suggest(self, ctx, *, args):
        channel = self.client.get_channel(737229481575448617)
        embed = discord.Embed(title=f'Suggestion from {ctx.author.name}!', description=f'{args}')
        await channel.send(embed=embed)
        await ctx.send(f'Thanks for your feedback!')
    
    @commands.command()
    async def whatsnew(self, ctx):
        if ctx.author.id == 420454043593342977:
            await ctx.message.delete()
            embed = discord.Embed(title=f'Update V{version}', description='''```
Main points this update:
    - Renamed to uwu bot (cos i like that better than JASON)
    - uwuify is now more uwu

More coming soon!
```''')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(BotBased(client))
