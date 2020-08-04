import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['helpme', 'commands'])
    async def help(self, ctx, *, args=None):
        try:
            if not args:
                embed = discord.Embed(title='uwu bot help uwu', color=0xfa00e9)
                embed.add_field(name='[]help fun', value='super fun commands help')
                embed.add_field(name='[]help mod', value='moderation commands help')
                embed.add_field(name='[]help util', value='Bot based commands')
                await ctx.send(embed=embed)

            if args == 'fun':
                embed = discord.Embed(title='Fun Commands Help page')
                embed.add_field(name='[]8ball (question)', value='Asks the magic 8ball a question')
                embed.add_field(name='[]coinflip', value='Flips a coin')
                embed.add_field(name='[]clap (text)', value='Sends text with *Sass*')
                embed.add_field(name='[]slap (@member)', value='Slaps a member')
                embed.add_field(name='[]hug (@member)', value='Hugs a member :)')
                embed.add_field(name='[]cuddle (@member)', value='Cuddles with a member.. aww :)')
                embed.add_field(name='[]kiss (@member)', value='Kiss a member :)')
                embed.add_field(name='[]poke (@member)', value='Poke someone')
                embed.add_field(name='[]gaymeter (@member)', value='Find out how gay you or your friends are!')
                embed.add_field(name='[]epicgamerrate (@member)', value='Find out how much of an epic gamer you and your friends are')
                embed.add_field(name='[]simpmeter (@member)', value='Find out how much of a simp you and your friends are')
                embed.add_field(name='[]google (question)', value='Shows you how to google something without asking me..')
                embed.add_field(name='[]uwuify (text)', value='(BETA) Makes text more uwu')
                embed.add_field(name='[]phcomment (comment)', value='Generate a fake pronhub comment')
                embed.add_field(name='[]ship (@member1) (@member2)', value='Get a love rating on two users, or a user and yourself')
                embed.add_field(name='[]tweet (username) (comment)', value='Generate a fake tweet with any username!')
                embed.add_field(name='[]bodypillow (@member)', value='Turn a user into a bodypillow')
                embed.add_field(name='[]baguette (@member)', value='Baguette') 
                embed.add_field(name='[]deepfry (@member)', value='Deepfry a users profile picture')
                embed.add_field(name='[]shitpost', value='Gets a random shitpost using r/copypasta')
                embed.add_field(name='[]changemymind (text)', value='Generates a ChangeMyMind meme with your text')
                embed.add_field(name='[]meme', value='Gets a meme from either r/dankmemes or r/animemes') #This is Field 22! Maximum of 25!
                await ctx.send(embed=embed)
                return
            elif args == 'mod':
                embed = discord.Embed(title='uwu bot moderation commands uwu', description='You need the correct permissions for each command. e.g ban_members for banning, manage_roles for muting etc.')
                embed.add_field(name='[]ban (@member) reason (optional)', value='Ban naughty people')
                embed.add_field(name='[]unban (user#0000)', value='Unban people that have learned their lesson')
                embed.add_field(name='[]mute (@member)', value='Mute people from chatting in the whole server')
                embed.add_field(name='[]unmute (@member)', value='Unmute people after they learn their lesson')
                embed.add_field(name='[]kick (@member)', value='Kicks a member from the server without banning them')
                embed.add_field(name='[]purge (2-100)', value='Delete up to 100 messages from the channel')
                embed.add_field(name='[]block (@member)', value='Block a member from chatting in the channel this command was used in, without muting the member')
                embed.add_field(name='[]unblock (@member)', value='Unblocks member from the channel')
                await ctx.send(embed=embed)
                return
            elif args == 'util':
                embed = discord.Embed(title='uwu bot utility commands uwu')
                embed.add_field(name='[]stats', value='Shows the uwu bot stats')
                embed.add_field(name='[]source', value='check uwu bots source code. pls dont steal ;-;')
                embed.add_field(name='[]ping', value='shows uwu bots ping to the discordboat api')
                embed.add_field(name='[]invite', value='invite uwu bot to your server')
                embed.add_field(name='[]suggest (suggestion)', value='suggest an uwu bot feature or command')
                await ctx.send(embed=embed)
            else:
                raise commands.BadArgument()
        except Exception as e:
            return

def setup(client):
    client.add_cog(help(client))