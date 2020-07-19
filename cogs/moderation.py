import discord
from discord.ext import commands
import asyncio

class mod(commands.Cog):
    def __init__(self, client):
        self.client = client 
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms', delete_after=2)
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'successfully kicked: {member} for reason: {reason}')
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'successfully banned: {member} for reason: {reason}')
        print(f'Member {member} banned with reason: {reason}')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_descriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_descriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Sucessfully unbanned {user}')
                print(f'Member unbanned: {member}')
                return
    
    @commands.command(aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=5):
        try:
            await ctx.send(f'Deleted {amount} messages!', delete_after=3)
            await ctx.channel.purge(limit=amount+1)
        
        except Exception as e:
            await ctx.channel.send('Could not delete messages! Make sure the messages are not more than 4 weeks old!')

    @commands.command(aliases=['stfu'])
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        try:
            role = discord.utils.get(ctx.author.guild.roles, name='Muted')
            await member.add_roles(role)
            embed = discord.Embed(description=f'Muted {member}!\n\nReason: {reason}')
            await ctx.send(embed=embed)
        except Exception as e:
            guild = ctx.guild
            await guild.create_role(name='Muted')
            role = discord.utils.get(ctx.author.guild.roles, name='Muted')
            embed = discord.Embed(description='Mute role not found. A new one has been created.')
            embed2 = discord.Embed(description='Please go to your server settings, go to roles and find the role titled "Muted"\nUnder its permissions, please set "Send messages" to "No"')
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)
            await member.add_roles(role)

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        try:
            role = discord.utils.get(ctx.author.guild.roles, name='Muted')
            await member.remove_roles(role)
            embed = discord.Embed(description=f'User unmuted: {member}')
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description=f'Unable to unmute {member}! Are they muted?')
            await ctx.send(embed=embed)

    @commands.command(aliases=['i'])
    async def userinfo(self, ctx, member : discord.Member):
        embed = discord.Embed(title=f'{member} info',  
            description="\uFEFF", 
            colour=ctx.author.colour, 
            timestamp=ctx.message.created_at) 
        embed.add_field(name='Username', value=member)
        embed.add_field(name='Nickname', value=member.nick)
        embed.add_field(name='ID', value=member.id)
        embed.add_field(name='Joined', value=member.joined_at)
        embed.add_field(name='Boosting Since', value=member.premium_since)
        embed.set_footer(text=f"Carpe Noctem | {self.client.user.name}")
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(mod(client))