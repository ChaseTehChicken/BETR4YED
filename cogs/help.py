import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['helpme', 'commands'])
    async def help(self, ctx):
        embed = discord.Embed(title='Command Help :)')
        embed.add_field(name='[]help', value='Shows this embed')
        embed.add_field(name='[]invite', value='Invite the bot to your server')
        embed.add_field(name='[]ping', value='Get the bots latency to the discord API')
        embed.add_field(name='[]8ball (question)', value='Asks the magic 8ball a question')
        embed.add_field(name='[]coinflip', value='Flips a coin')
        embed.add_field(name='[]clap (text)', value='Sends text with *Sass*')
        embed.add_field(name='[]slap (@member)', value='Slaps a member')
        embed.add_field(name='[]hug (@member)', value='Hugs a member :)')
        embed.add_field(name='[]cuddle (@member)', value='Cuddles with a member.. aww :)')
        embed.add_field(name='[]kiss (@member)', value='Kiss a member :)')
        embed.add_field(name='[]poke (@member)', value='Poke someone')
        embed.add_field(name='[]ghost @member', value='Ghost a ping a member up to 20 times')
        embed.add_field(name='[]gaymeter (@member)', value='Find out how gay you or your friends are!')
        embed.add_field(name='[]epicgamerrate (@member)', value='Find out how much of an epic gamer you and your friends are')
        embed.add_field(name='[]simpmeter (@member)', value='Find out how much of a simp you and your friends are')
        embed.add_field(name='[]google (question)', value='Shows you how to google something without asking me..')
        embed.add_field(name='[]uwuify (text)', value='(BETA) Makes text more uwu')
        embed.add_field(name='[]stats', value='Get the bot stats')
        embed.add_field(name='[]source', value='Sends a link to the bots source code!')
        embed.add_field(name='[]suggest', value='Suggest new bot features')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(help(client))