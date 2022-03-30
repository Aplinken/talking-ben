import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True,case_insensitive=True)
    async def help(self,ctx):
        embed = discord.Embed(title='Help',color = discord.Colour.blue())

        embed.add_field(name='Text',value='`ben`,`ans`,`source`,`ping`,`leaderboard`')
        embed.add_field(name='Voice',value='`vc`,`leave`')
        embed.set_footer(text='aplinken.03')

        await ctx.send(embed=embed)

    @help.command()
    async def ben(self,ctx):
        em = discord.Embed(title="Ben",description="ben answers your questions",color=discord.Color.green())
        em.add_field(name="**Syntax**", value="~ben <question>")
        await ctx.send(embed=em)

    @help.command()
    async def ans(self,ctx):
        em = discord.Embed(title="Ans",description="ben tells you the amount of questions he has answered in the server and for you",color=discord.Color.green())
        em.add_field(name="**Syntax**", value="~ans")
        await ctx.send(embed=em)    

    @help.command()
    async def source(self,ctx):
        em = discord.Embed(title="Source",description="source code of the bot",color=discord.Color.green())
        em.add_field(name="**Syntax**", value="~source")
        await ctx.send(embed=em)

    @help.command()
    async def ping(self,ctx):
        em = discord.Embed(title="Ping",description="ben tells you his reaction speed",color=discord.Color.green())
        em.add_field(name="**Syntax**", value="~ping")
        await ctx.send(embed=em)

    @help.command()
    async def vc(self,ctx):
        em = discord.Embed(title="VC",description="ben answers your questions in vc `you must be connected to a vc first`",color=discord.Color.green())
        em.add_field(name="**Syntax**", value="~vc")
        await ctx.send(embed=em)    

    @help.command()
    async def leave(self,ctx):
        em = discord.Embed(title="Leave",description="ben leaves any vc he is connected to",color=discord.Color.green())
        em.add_field(name="**Syntax**", value="~leave")
        await ctx.send(embed=em)

    @help.command(aliases=['lb'])
    async def leaderboard(self,ctx):
        em = discord.Embed(title="Leaderboard",description="ben shows global leaderboard",color=discord.Color.green())
        em.add_field(name="**Syntax**", value="~leaderboard/~lb")
        await ctx.send(embed=em)



def setup(client):
	client.add_cog(Help(client))
