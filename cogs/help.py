import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['helpme'])
    async def help(self, ctx):
        await ctx.send('''```css
        BETR4YED COMMANDS
        Bot Based:
            Help --- Shows this message
            Stats --- Shows bot stats
        Custom Games:
            Rules --- Shows the default rules for Bets customs
            Mod --- How to get moderator on bets youtube channel
            Joingame --- Shows how to join Bets game
        Fun:
            8Ball --- Roll the 8ball to decide your fate
            Coinflip --- Basically 8ball but its yes or no
            Kill --- Kill a user
        Socials:
            Creator Code --- Shows Bets creator code #Ad
            Insta --- Sends a link too Bets instagram
            Epic --- Sends Bets Epic Games username in chat
            PSN --- Sends Bets Playstation Network username in chat
            Twitter --- Sends a link to Bets Twitter in chat
            Youtube --- Sends a link to YouTube channel in chat
        Stream Based:
            Join --- Sends a link to become a member of Bets youtube channel
            Subscribe --- Sends a link to Subscribe to Bets youtube channel
            Twitch --- Sends a link to Bets twitch channel in chat
        
        --- MODERATOR ONLY COMMANDS ---
        These commands dont work for all users because no :)
            Kick [user] --- Kicks specified user from server
            ban [user] --- Bans specified user from server
            unban [user] --- Unbans user from server
            Purge [2 - 99] --- Deletes specified amount of messages from the channel the command was user in```''')

def setup(client):
    client.add_cog(help(client))