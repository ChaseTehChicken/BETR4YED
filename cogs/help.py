import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['helpme'])
    async def help(self, ctx, *, helpType=None):
        if helpType == None:
            embed = discord.Embed(title='Help for JASON')
            embed.add_field(name='[]help Mod', value='Help with the moderator commands', inline=True)
            embed.add_field(name='[]help Fun', value='Help with the Fun commands', inline=True)
            embed.add_field(name='[]help Bot', value='Help with the Bot Based commands', inline=True)
            await ctx.send(embed=embed)
        elif helpType == 'mod':
            embed = discord.Embed(title='Moderation Commands on JASON')
            embed.add_field(name='Ban @user#0420 [reason]', value='Bans a member', inline=True)
            embed.add_field(name='Unban user#0420', value='Unbans a member', inline=True)
            embed.add_field(name='Kick @user#0420', value='Kick a user from the server, without banning them', inline=True)
            embed.add_field(name='Purge [2-200]', value='Purges up to 200 messages from the channel', inline=True)
            embed.add_field(name='Mute @user#0420', value='Gives a member the mute role', inline=True)
            embed.add_field(name='Unmute @user#0420', value='Removes mute role from user', inline=True)
            embed.add_field(name='userinfo @user#0420', value='Get information on a specific user', inline=True)
            await ctx.send(embed=embed)
        elif helpType == 'fun':
            embed = discord.Embed(title='Fun Commands on JASON')
            embed.add_field(name='8Ball [question]', value='Ask the 8ball a question')
            embed.add_field(name='coinflip', value='Flip a coin')
            embed.add_field(name='Optout', value='Optout of the Rules of any given server (bans you)')
            embed.add_field(name='ghost', value='Ghost ping any member of the server! Ping them between 5 and 20 times')
            await ctx.send(embed=embed)
        elif helpType == 'bot':
            embed = discord.Embed(title='Bot Commands')
            embed.add_field(name='Stats', value='Shows you the bot stats')
            embed.add_field(name='Ping', value='Shows the bots ping')
            embed.add_field(name='github', value='Sends a link to the source code for the bot')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description='Please choose a valid help option')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(help(client))