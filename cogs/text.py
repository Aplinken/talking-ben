from turtle import color
import discord
from discord.ext import commands
import random

reply_list = ['Yes.','No.','Hohoho','Ugh'] #List of possible replies

class Text(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def ben(self,ctx,q=None):
        if q is None:
            await ctx.send('Ben') #Bruh Ben
        else:
            await ctx.send(random.choice(reply_list)) #Random Reply

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


def setup(client):
	client.add_cog(Text(client))