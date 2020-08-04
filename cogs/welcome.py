import discord
from discord.ext import commands
import sqlite3
import datetime

class welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {member.guild.id}")
        result = cursor.fetchone()
        if result is None:
            return
        else:
            cursor.execute(f"SELECT msg FROM main WHERE guild_id = {member.guild.id}")
            result1 = cursor.fetchone()
            members = len(list(member.guild.members))
            mention = member.mention
            user = member.name
            guild = member.guild
            embed = discord.Embed(description=str(result1[0]).format(members=members, mention=mention, user=user, guild=guild))
            embed.set_thumbnail(url=f'{member.avatar_url}')
            embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
            embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')
            embed.timestamp = datetime.datetime.utcnow()

            channel = self.client.get_channel(id=int(result[0]))

            await channel.send(embed=embed)

    @commands.group(invoke_without_command=True)
    async def welcome(self, ctx):
        await ctx.send('Setup Commands:\nwelcome channel <#channel>\nwelcome text <message>')

    @welcome.command()
    @commands.has_permissions(manage_messages=True)
    async def channel(self, ctx, channel:discord.TextChannel):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {ctx.guild.id}")
        results = cursor.fetchone()
        if results is None:
            sql = ("INSERT INTO main(guild_id, channel_id) VALUES(?, ?)")
            val = (ctx.guild.id, channel.id)
            await ctx.send(f'Channel has been set to {channel.mention}')
        elif results is not None:
            sql = ("UPDATE main SET channel_id =? WHERE guild_id = ?")
            val = (channel.id, ctx.guild.id)
            await ctx.send(f'Channel has been updated to {channel.mention}')
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()

    @welcome.command()
    @commands.has_permissions(manage_messages=True)
    async def text(self, ctx, *, msg):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT msg FROM main WHERE guild_id = {ctx.guild.id}")
        results = cursor.fetchone()
        if results is None:
            sql = ("INSERT INTO main(guild_id, msg) VALUES(?, ?)")
            val = (msg, channel.id)
            await ctx.send(f'Welcome text has been set to: `{msg}`')
        elif results is not None:
            sql = ("UPDATE main SET msg =? WHERE guild_id = ?")
            val = (msg, ctx.guild.id)
            await ctx.send(f'Welcome text has been updated to: ``{msg}``')
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()

def setup(client):
    client.add_cog(welcome(client))