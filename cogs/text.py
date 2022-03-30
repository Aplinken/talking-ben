import asyncpg
import discord
from discord.ext import commands
import random
import os

reply_list = ['Yes.','No.','Hohoho','Ugh'] #List of possible replies

async def update_ans(guild):
    db = await asyncpg.connect(f"{os.environ.get('DATABASE')}")
    result = await db.fetch(f'''
        SELECT * FROM main WHERE guild_id = {guild}
    ''')
    if result is None:
        await db.execute(f'''
            INSERT INTO main (guild_id, answered) VALUES ({guild},1)
        ''')
    else:     
        await db.execute(f'''
            UPDATE main SET answered = answered + 1 WHERE guild_id = {guild} 
        ''')
    await db.close()    

class Text(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def ben(self, ctx, q = None):
        if not q:
            return await ctx.send('Ben') #Bruh Ben

        await update_ans(ctx.guild.id)
        await ctx.send(random.choice(reply_list)) #Random Reply
 
    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title='Help',color = discord.Colour.blue())
        embed.add_field(name='Ben',value='Use this command to ask ben questions\n*Syntax: ~ben <question>*',inline=False)
        embed.add_field(name='VC',value='Use this command to ask ben questions in vc(also used for joining vc)\n*Syntax: ~vc*',inline=False)
        embed.set_footer(text='aplinken.02')
        await ctx.send(embed=embed)

    @commands.command()
    async def source(self,ctx):
        await ctx.send("https://github.com/Aplinken/talking-ben")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'My ping is: {round(ctx.bot.latency * 1000)}ms')

    @commands.command()
    async def ans(self,ctx):
        guild = ctx.guild.id
        db = await asyncpg.connect(f"{os.environ.get('DATABASE')}")
        result = await db.fetch(f'''
            SELECT answered FROM main WHERE guild_id = {guild} LIMIT 1
        ''')
        fm_result = str(result)

        await ctx.send(f"Amount Of Questions Answered: {fm_result[1:-2]}")
        await db.close()
        


def setup(client):
	client.add_cog(Text(client))
