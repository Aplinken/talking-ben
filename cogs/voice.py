import random
import asyncio
import asyncpg
import os
from xmlrpc import client
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from .text import update_ans

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
            await voice.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(f"./cogs/audio/{reply}")))
            update_ans(guild=ctx.guild.id)
         
def setup(client):
	client.add_cog(Voice(client))
