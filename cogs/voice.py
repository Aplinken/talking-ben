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
        voice = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild) 

        if voice is None: #JOIN VC   
            channel = ctx.author.voice.channel
            if channel is None:
                await ctx.send("You are not connected to any voice channels!")
            else:
                await channel.connect()
        else:
            reply = random.choice(vc_reply_list)                                        
            voice.play(
		    PCMVolumeTransformer(FFmpegPCMAudio(f"./cogs/audio/{reply}"))
	    	)
            await update_ans(guild=ctx.guild.id)
         
def setup(client):
	client.add_cog(Voice(client))
