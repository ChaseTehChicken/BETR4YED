import discord
from discord.ext import commands

class mod(commands.Cog):
    def __init__(self, client):
        self.client = client 
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms')
    
    @commands.command()
    @commands.has_permissions(manage_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'successfully kicked: {member} for reason: {reason}')
    @commands.command()
    @commands.has_permissions(manage_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'successfully banned: {member} for reason: {reason}')
        print(f'Member {member} banned with reason: {reason}')

    @commands.command()
    @commands.has_permissions(manage_members=True)
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
        await ctx.channel.purge(limit=amount+1)

    @commands.command(aliases=['stfu'])
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        role = discord.utils.get(ctx.author.guild.roles, name='Muted')
        await member.add_roles(role)
        await ctx.send(f'Mute role added to {member}!')


    
    
def setup(client):
    client.add_cog(mod(client))
