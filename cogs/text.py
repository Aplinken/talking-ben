import asyncpg
import discord
from discord.ext import commands
import random
import os

reply_list = ['Yes.','No.','Hohoho','Ugh'] #List of possible replies

async def update_ans(guild,player_id,player_name): #add +1 to answered VALUE that matches guild_id 

    #guild based

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

    #player based

    result_2 = await db.fetchval(f'''
        SELECT * FROM player WHERE id = {player_id}
    ''')
    if result_2 is None:
        await db.execute(f'''
            INSERT INTO player (id, answered, name) VALUES ({player_id}, 1, '{player_name}')
        ''')
    else:     
        await db.execute(f'''
            UPDATE player SET answered = answered + 1 WHERE id = {player_id} 
        ''')

    await db.close()    

class Text(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def ben(self, ctx, q = None):
        if not q:
            return await ctx.send('Ben') #Bruh Ben

        await update_ans(ctx.guild.id,ctx.author.id,ctx.author.name)
        await ctx.send(random.choice(reply_list)) #Random Reply

    @commands.command()
    async def source(self,ctx):
        await ctx.send("https://github.com/Aplinken/talking-ben")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'My ping is: {round(ctx.bot.latency * 1000)}ms')

    @commands.command()
    async def ans(self,ctx):
        guild = ctx.guild.id
        player_id = ctx.author.id
        db = await asyncpg.connect(f"{os.environ.get('DATABASE')}")
        result = await db.fetch(f'''
            SELECT answered FROM main WHERE guild_id = {guild} LIMIT 1
        ''')
        fm_result = str(result)

        await ctx.send(f"Amount Of Questions Answered In This Server: {fm_result[18:-2]}")

        result_2 = await db.fetch(f'''
            SELECT answered FROM player WHERE id = {player_id} LIMIT 1
        ''')
        fm_result_2 = str(result_2)

        await ctx.send(f"\nAmount Of Questions From You That I Answered: {fm_result_2[18:-2]}")
        await db.close()

    @commands.command(aliases=['lb'])
    async def leaderboard(self,ctx):
        player_id = ctx.author.id

        db = await asyncpg.connect(f"{os.environ.get('DATABASE')}")
        result = await db.fetch(f'''
            SELECT answered, name FROM player ORDER BY answered DESC, name DESC LIMIT 10
        ''')
        
        em = discord.Embed(title='Leaderboard')
        for i, pos in enumerate(result, start=1):
            ans, name = pos
            print(f"{i}. {name}, Answered: {ans}")
            em.add_field(name=f"{i}. {name}",value=f"Answered: {ans}")

        await ctx.send(embed=em)


        


def setup(client):
	client.add_cog(Text(client))
