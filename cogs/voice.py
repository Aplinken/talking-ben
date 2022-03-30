import random
from .text import update_ans

import discord
from discord.ext import commands
from discord import PCMVolumeTransformer, FFmpegPCMAudio

vc_reply_list = ['Laugh.wav','Yes.wav','No.wav','Ugh.wav']

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def vc(self,ctx):
        if ctx.author.voice is None:
            return await ctx.send("You are not connected to any voice channels!")

        if ctx.voice_client is None: #JOIN VC
            await ctx.author.voice.channel.connect()
            await ctx.send("Joined the voice channel")
                          
        reply = random.choice(vc_reply_list)                                        
        ctx.voice_client.play(
	       PCMVolumeTransformer(FFmpegPCMAudio(f"./cogs/audio/{reply}"))
    	)
        await update_ans(guild=ctx.guild.id,player_id=ctx.author.id,player_name=ctx.author.name)
        
    @commands.command()
    async def leave(self,ctx):
        if ctx.voice_client is None:
            return await ctx.send("I'm not connected to any voice channels.") 

        await ctx.voice_client.disconnect()
        await ctx.send("Left the voice channel")
         
def setup(client):
	client.add_cog(Voice(client))
