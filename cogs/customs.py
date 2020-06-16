import discord
from discord.ext import commands

class CustomGames(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def rules(self, ctx):
        await ctx.send('```NO STREAM SNIPING PLEASE. NO ELIM UNTIL START OF 2ND ZONE. NO TOXICITY. ATTACKING TOXIC PLAYERS IS ALLOWED```')
        print(f'{ctx.author.name} used command Rules')

    @commands.command()
    async def mod(self, ctx):
        await ctx.send('To become a Moderator on YouTube, stay active, help chat and be respectful. \nTo become a moderator on discord, stay active, be respectful and DO NOT MINIMOD!')
        print(f'{ctx.author.name} used command Mod')
    
    @commands.command()
    async def joingame(self, ctx):
        await ctx.send('To join Bets game, enter the code shown on stream before each game')
        print(f'{ctx.author.name} used command JoinGame')
        
def setup(client):
    client.add_cog(CustomGames(client))