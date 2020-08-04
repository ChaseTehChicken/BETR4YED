# Now this is a big OwO moment
import discord
from discord.ext import commands
import random
import json
import random
import aiohttp
import nekos
import asyncio
import uwuify

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client 
        self.session = aiohttp.ClientSession()

    def __embed_json(self, data, key="message"):
        em = discord.Embed(color=0xDEADBF)
        em.set_image(url=data[key])
        return em 
    
    async def __get_image(self, ctx, user=None):
        if user:
            if user.is_avatar_animated():
                return str(user.avatar_url_as(format="gif"))
            else:
                return str(user.avatar_url_as(format="png"))

        await ctx.trigger_typing()

        message = ctx.message

        if len(message.attachments) > 0:
            return message.attachments[0].url

        def check(m):
            return m.channel == message.channel and m.author == message.author

        try:
            await ctx.send("Send me an image!")
            x = await self.client.wait_for('message', check=check, timeout=15)
        except:
            return await ctx.send("Timed out...")

        if not len(x.attachments) >= 1:
            return await ctx.send("No images found.")

        return x.attachments[0].url


    @commands.command(aliases=["8ball"])
    async def _ball(self, ctx, *, question):
        try:
            if question == 'yes':
                responses = ['yes']
                await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
            else:
                responses = ['yes',
                'maybe',
                'no',
                'idk, maybe?',
                'What kind of stupid question is that',
                'No chance bud']
                await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
        except Exception as e:
            embed = discord.Embed(description='Please ask a question for the 8ball\n\nCorrect usage: []8ball [question]')
            await ctx.send(embed=embed)

    @commands.command()
    async def coinflip(self, ctx):
        HeadsTails = ['Heads',
        'Tails']
        await ctx.send(f'{random.choice(HeadsTails)}')
    
    @commands.command()
    async def optout(self, ctx):
        embed = discord.Embed(
            title = f'{ctx.message.author} has opted out',
            description = f'{ctx.message.author} has opted out of the discord ToS and has been banned from the server!'
        )
        await ctx.send(embed=embed)
        await ctx.author.ban(reason='Opt out lmao')

    @commands.command()
    async def rr(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    @commands.command()
    async def slap(self, ctx, *, member : discord.Member):
        slap = nekos.img('slap')
        try:
            if not member:
                embed = discord.Embed(description='Please specify a member to beat the shit out of')
                await ctx.send(embed=embed)
            
            if member.id == ctx.author.id:
                embed = discord.Embed(
                    title=f'{ctx.author.name} slapped themselves! Ouch..'
                )
                embed.set_image(url=slap)
                await ctx.send(embed=embed)
            else:
                slap = nekos.img('slap')
                embed = discord.Embed(title=f'{ctx.author.name} slapped {member.name}! Ouch!')
                embed.set_image(url=slap)
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description='We\'ve run into an error. Please make sure you specify a member to slap')
            await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, member : discord.Member=None):
        hug = nekos.img('hug')
        try:
            if not member:
                embed = discord.Embed(description='Please mention a user to hug :3\nCorrect usage: []hug @user')
                await ctx.send(embed=embed, delete_after=5) 
            elif member.id == ctx.author.id:
                embed=discord.Embed(description=f'{ctx.author.name} hugs themselves! How cute :hearts:')
                embed.set_image(url=hug)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(description=f'{ctx.author.name} hugs {member.name}! How cute :hearts:')
                embed.set_image(url=hug)
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description='There was a problem with your command. Remember to specify someone to hug')
            await ctx.send(embed=embed)

    @commands.command()
    async def cuddle(self, ctx, member : discord.Member=None):
        cuddle = nekos.img('cuddle')
        try:
            if not member:
                embed = discord.Embed(description='Please mention a user to cuddle :3\nCorrect usage: []cuddle @user')
                await ctx.send(embed=embed, delete_after=5)
            elif member.id == ctx.author.id:
                embed=discord.Embed(description=f'{ctx.author.name} cuddles themself. How cuute :hearts:')
                embed.set_image(url=cuddle)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(description=f'{ctx.author.name} cuddles {member.name}! How cute :hearts:')
                embed.set_image(url=cuddle)
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description='There was a problem with your command. Specify a member to cuddle, and try again')
            await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member : discord.Member=None):
        kissgif = nekos.img('kiss')
        try:
            if not member:
                embed = discord.Embed(description='Please mention a user to kiss :3\nCorrect usage: []kiss @user')
                await ctx.send(embed=embed, delete_after=5)
            elif member.id == ctx.author.id:
                embed = discord.Embed(description=f'{ctx.author.name} kisses them self, how cute :hearts:')
                embed.set_image(url=kissgif)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'{ctx.author.name} kisses {member.name}! How cute :hearts:')
                embed.set_image(url=kissgif)
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description='There was a problem with your command. Specify a member to kiss, and try again')
            await ctx.send(embed=embed)

    @commands.command()
    async def poke(self, ctx, member : discord.Member=None):
        poke = nekos.img('poke')
        try:
            if not member:
                embed = discord.Embed(description='Please mention a user to poke :3\nCorrect usage: []poke @user')
                await ctx.send(embed=embed, delete_after=5)
            elif member.id == ctx.author.id:
                embed = discord.Embed(description=f'{ctx.author.name} pokes themself.. weird.. :hearts:')
                embed.set_image(url=poke)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'{ctx.author.name} pokes {member.name}... :hearts:')
                embed.set_image(url=poke)
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description='There was a problem with your command. Specify a member to poke, and try again')

    # @commands.command()
    # async def ghost(self, ctx, member : discord.Member=None, amount=5):
    #     try:
    #         if ctx.author.id != 420454043593342977:
    #             if not member:
    #                 embed = discord.Embed(description="Please specify a server member to ping!")
    #                 await ctx.send(embed=embed)
    #             elif amount <= 5:
    #                 embed = discord.Embed(description='Please choose a number between 5 and 20')
    #                 await ctx.send(embed=embed)
    #             elif amount > 20:
    #                 embed = discord.Embed(description="This bot cannot ghost ping people more than 20 times")
    #                 await ctx.send(embed=embed)
    #             else:
    #                 msg = ctx.message
    #                 await msg.delete()
    #                 for i in range(1, amount+1):
    #                     await ctx.send(f'<@{member.id}>', delete_after=1)
    #         else:
    #             if not member:
    #                 embed = discord.Embed(description="Please specify a server member to ping!")
    #                 await ctx.send(embed=embed)
    #             elif amount <= 5:
    #                 embed = discord.Embed(description='Please choose a number between 5 and 20')
    #                 await ctx.send(embed=embed)
    #             else:
    #                 msg = ctx.message
    #                 await msg.delete()
    #                 for i in range(1, amount+1):
    #                     await ctx.send(f'<@{member.id}>', delete_after=1)
    #     except Exception as e:
    #         embed = discord.Embed(description='Sorry, we seem to have ran into an error. Remember to specify a member to ping, if the problem persists, contact Chaseyy#9999 for more info')
    #         await ctx.send(embed=embed)

    @commands.command()
    async def gaymeter(self, ctx, member : discord.Member=None):
        try:
            if not member:
                embed = discord.Embed(description=f'{ctx.author.name}, you are {random.randint(0,101)}% gay\n:rainbow_flag:')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'{member.name} is {random.randint(0,101)}% gay\n:rainbow_flag:')
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description=f'We have ran into an error. Error code: {e}\nContact Chaseyy#9999 for support')
            await ctx.send(embed=embed)
    
    @commands.command()
    async def epicgamerrate(self, ctx, member : discord.Member=None):
        try:
            if not member:
                embed = discord.Embed(description=f'{ctx.author.name}, you are {random.randint(1,101)}% Epic')
                await ctx.send(embed=embed)
            elif member.id == ctx.author.id:
                embed = discord.Embed(description=f'{ctx.author.name}, you are {random.randint(1,101)}% Epic')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'{member.name}, you are {random.randint(1,101)}% Epic')
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description=f'We have ran into an error. Error code: {e}\nContact Chaseyy#9999 for support')

    @commands.command()
    async def simpmeter(self, ctx, member : discord.Member=None):
        try:
            if not member:
                embed = discord.Embed(description=f'{ctx.author.name} is {random.randint(0, 101)}% simp')
                await ctx.send(embed=embed)
            elif member.id == ctx.author.id:
                embed = discord.Embed(description=f'{ctx.author.name} is {random.randint(0, 101)}% simp')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'{member.name} is {random.randint(0, 101)}% simp')
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description=f'We have ran into an error. Error code: {e}\nContact Chaseyy#9999 for support')
            await ctx.send(embed=embed)

    @commands.command()
    async def clap(self, ctx, *, args):
        try:
            if not ' ' in args:
                charList = [char for char in args]
                sendText = ' '.join(map(str, charList))
                await ctx.send(sendText.replace(' ', ' :clap: '))
                return
            await ctx.send(args.replace(' ', ' :clap: '))
        except Exception as e:
            embed = discord.Embed(description=f'We have ran into an error (probably out of hands to clap with). Error code: {e}\nContact Chaseyy#9999 for support')
            await ctx.send(embed=embed)

    @commands.command()
    async def google(self, ctx, *, args):
        try:
            if not ' ' in args:
                await ctx.send(f'<http://lmgtfy.com/?q={args}&pp=1>')
                return
            await ctx.send(f"<http://lmgtfy.com/?q={args.replace(' ', '+')}&pp=1>")
        except Exception as e:
            embed = discord.Embed(description=f'That question was too hard to google.. Error code: {e}\nContact Chaseyy#999 for support')
            await ctx.send(embed=embed)

    @commands.command()
    async def uwuify(self, ctx, *, args):
        flags = uwuify.SMILEY | uwuify.YU
        await ctx.send(uwuify.uwu(args, flags=flags))

    @commands.command()
    async def tweet(self, ctx, username: str, *, text: str):
        await ctx.trigger_typing()
        async with self.session.get('https://nekobot.xyz/api/imagegen?type=tweet'
                                    '&username=%s'
                                    '&text=%s' % (username, text,)) as r:
            res = await r.json()
        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def phcomment(self, ctx, *, comment : str):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send('This channel must be marked NSFW to use this command ;)')
        await ctx.trigger_typing()
        async with self.session.get(f'https://nekobot.xyz/api/imagegen?type=phcomment'
                                    f'&image={ctx.author.avatar_url_as(format="png")}'
                                    f'&text={comment}&username={ctx.author.name}') as r:
            res = await r.json()
        if not res["success"]:
            return await ctx.send('**Failed to get image ;-;')
        await ctx.send(embed=self.__embed_json(res))

    @commands.command(aliases=['lovemeter'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ship(self, ctx, user1: discord.Member, user2: discord.Member = None):
        if user2 is None:
            user2 = ctx.author
        await ctx.trigger_typing()
        if user1.avatar:
            user1url = "https://cdn.discordapp.com/avatars/%s/%s.png" % (user1.id, user1.avatar,)
        else:
            user1url = "https://cdn.discordapp.com/embed/avatars/1.png"
        if user2.avatar:
            user2url = "https://cdn.discordapp.com/avatars/%s/%s.png" % (user2.id, user2.avatar,)
        else:
            user2url = "https://cdn.discordapp.com/embed/avatars/1.png"

        self_length = len(user1.name)
        first_length = round(self_length / 2)
        first_half = user1.name[0:first_length]
        usr_length = len(user2.name)
        second_length = round(usr_length / 2)
        second_half = user2.name[second_length:]
        finalName = first_half + second_half

        score = random.randint(0, 100)
        filled_progbar = round(score / 100 * 10)
        counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)

        async with self.session.get("https://nekobot.xyz/api/imagegen?type=ship&user1=%s&user2=%s" % (user1url, user2url,)) as r:
            res = await r.json()

        em = discord.Embed(color=0xDEADBF)
        em.title = "%s ❤ %s" % (user1.name, user2.name,)
        em.description = f"**Love %**\n" \
                         f"`{counter_}` **{score}%**\n\n{finalName}"
        em.set_image(url=res["message"])

        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bodypillow(self, ctx, user : discord.Member):
        await ctx.trigger_typing()
        img = await self.__get_image(ctx, user)
        if not isinstance(img, str):
            return img
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=bodypillow&url=%s" % img) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def baguette(self, ctx, user:discord.Member):
        await ctx.trigger_typing()
        avatar = user.avatar_url_as(format="png")
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=baguette&url=%s" % avatar) as r:
            res = await r.json()
        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def deepfry(self, ctx, user:discord.Member=None):
        img = await self.__get_image(ctx, user)
        if not isinstance(img, str):
            return img
        
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=deepfry&image=%s" % img) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def shitpost(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.send('Use this in an NSFW channel pls ;)')

        await ctx.trigger_typing()
        try:
            async with self.session.get("https://www.reddit.com/r/copypasta/hot.json?sort=hot") as r:
                res = await r.json()

            data = random.choice(res["data"]["children"])["data"]
            em = discord.Embed(color=0xDEADBF, title=data["title"], description=data["selftext"], url=data["url"])
            em.set_footer(text="👍 - %s upvotes" % data["ups"])
            await ctx.send(embed=em)

        except Exception as e:
            await ctx.send("Failed to get data, %s" % e)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def changemymind(self, ctx, *, text: str):
        await ctx.trigger_typing()

        async with self.session.get("https://nekobot.xyz/api/imagegen?type=changemymind&text=%s" % text) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx):
        sub = ["dankmemes", "animemes"] 
        url = f'https://api.imgur.com/3/gallery/r/{random.choice(sub)}/hot/{random.randint(1, 5)}'
        headers = {"Authorization": f"Client-ID {config.imgur}"}
        async with self.session.get(url, headers=headers) as r:
            res = await r.json()
        if res["status"] == 429:
            return await ctx.send("**Ratelimited, try again later.**")
        js = random.choice(res['data'])
        f = False
        if js['nsfw'] or js['is_ad']:
            for x in res["data"]:
                if not js['nsfw'] or not js['is_ad']:
                    js = x
                    f = True
                    break
        else:
            f = js
        if not f:
            return await ctx.send("Nothing found")
        embed = discord.Embed(color=0xDEADBF,
                              description=f"**{js['title']}**")
        embed.set_image(url=js['link'])
        time = datetime.datetime.fromtimestamp(int(js['datetime'])).strftime('%Y-%m-%d %H:%M')
        embed.set_footer(text=f"Posted on {time}")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def changemymind(self, ctx, *, text: str):
        await ctx.trigger_typing()

        async with self.session.get("https://nekobot.xyz/api/imagegen?type=changemymind&text=%s" % text) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))

def setup(client):
    client.add_cog(fun(client))