import discord
from discord.ext import commands

global muted

class Sinner(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument)
        permission = argument.guild_permissions.manage_messages 
        if not permission: 
            return argument 
        else:
            raise commands.BadArgument("You cannot punish other staff members")

class Redeemed(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument)
        muted = discord.utils.get(ctx.guild.roles, name="Muted") 
        if muted in argument.roles: 
            return argument 
        else:
            raise commands.BadArgument("The user was not muted.")
            
async def mute(ctx, user, reason):
    role = discord.utils.get(ctx.guild.roles, name="Muted") 
    if not role: 
        try: 
            muted = await ctx.guild.create_role(name="Muted", reason="To use for muting")
            for channel in ctx.guild.channels: 
                await channel.channel.set_permissions(muted, send_messages=False,
                                                read_message_history=False,
                                                read_messages=False)
        except discord.Forbidden:
            return await ctx.send("I have no permissions to make a muted role")
        await user.add_roles(muted) 
        await ctx.send(f"{user.mention} has been muted for {reason}")
    else:
        await user.add_roles(role) 
        await ctx.send(f"{user.mention} has been muted for {reason}")

class Moderation(commands.Cog):    
    def __init__(self, client):
        self.client = client

    async def __error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : Sinner=None, *, reason=None):
        if not member:
            return await ctx.send('You must specify a user to ban')

        try:
            await member.ban(reason=reason)
            await ctx.send(f'{member.name} was banned ;-;\nReason: {reason}')

        except discord.Forbidden:
            return await ctx.send('Are you trying to ban someone higher than me? I cant do that ;-;')

    @commands.command()
    @commands.has_permissions(ban_members=True)
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

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, user: Sinner, reason=None):
        await mute(ctx, user, reason or "treason") 
        await ctx.send(f'{user} was muted for {reason}')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: Sinner=None, reason=None):
        if not user: 
            return await ctx.send("You must specify a user")

        try: 
            await ctx.guild.kick(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified")
            await ctx.send(f'{user} was kicked for {reason}')
        except discord.Forbidden:
            return await ctx.send("Are you trying to kick someone higher than the bot?")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):

        await ctx.purge(limit=limit + 1) 
        await ctx.send(f"Bulk deleted `{limit}` messages", delete_after=5) 

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, user: Redeemed):
        await user.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted"))
        await ctx.send(f"{user.mention} has been unmuted")
        return

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def block(self, ctx, user: Sinner=None):

        if not user: 
            return await ctx.send("You must specify a user")

        await ctx.channel.set_permissions(user, send_messages=False)
        await ctx.send(f'{user} was blocked from sending messages in this channel ;-;')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unblock(self, ctx, user: Sinner=None):

        if not user: 
            return await ctx.send("You must specify a user")
        
        await ctx.channel.set_permissions(user, send_messages=True)
        await ctx.channel.send(f'{user} was unblocked in the channel :D')

def setup(client):
    client.add_cog(Moderation(client))