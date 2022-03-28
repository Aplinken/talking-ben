import sqlite3
import discord
from discord.ext import commands
import random

reply_list = ['Yes.','No.','Hohoho','Ugh'] #List of possible replies

class Text(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def ben(self,ctx,q=None):
        guild = ctx.guild.id
        if q is None:
            await ctx.send('Ben') #Bruh Ben
        else:
            db = sqlite3.connect('data.sqlite')
            cursor = db.cursor()
            cursor.execute(f'''
                SELECT * FROM main WHERE guild_id = {guild}
            ''')
            result = cursor.fetchone()
            if result is None:
                cursor.execute(f'''
                    INSERT INTO main (guild_id, answered) VALUES ({guild},1)
                ''')
            else:     
                cursor.execute(f'''
                    UPDATE main SET answered = answered + 1 WHERE guild_id = {guild} 
                ''')

            await ctx.send(random.choice(reply_list)) #Random Reply
            db.commit()
            cursor.close()

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title='Help',color = discord.Colour.blue())
        embed.add_field(name='Ben',value='Use this command to ask ben questions\n*Syntax: ~ben <question>*',inline=False)
        embed.add_field(name='VC',value='Use this command to ask ben questions in vc(also used for joining vc)\n*Syntax: ~vc*',inline=False)
        embed.set_footer(text='aplinken.02')
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'My ping is: {round(ctx.bot.latency * 1000)}ms')

    @commands.command()
    async def ans(self,ctx):
        guild = ctx.guild.id
        db = sqlite3.connect('data.sqlite')
        cursor = db.cursor()
        cursor.execute(f'''
            SELECT answered FROM main WHERE guild_id = {guild}
        ''')
        result = cursor.fetchone()
        fm_result = str(result)

        await ctx.send(f"Amount Of Questions Answered: {fm_result[1:-2]}")
        


def setup(client):
	client.add_cog(Text(client))
