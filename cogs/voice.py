import random
import os
from xmlrpc import client
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

vc_reply_list = ['Laugh.wav','Yes.wav','No.wav','Ugh.wav']

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def vc(self,ctx):
        voice = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild) 

        if voice is None: #JOIN VC   
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            reply = random.choice(vc_reply_list)
            print(reply)                                              
            voice.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(f"./audio/{reply}")))
         
def setup(client):
	client.add_cog(Voice(client))
