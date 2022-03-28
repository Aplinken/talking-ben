import discord
from discord.ext import commands
import os

ownerid = 742661420683886597

# Client created
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=commands.when_mentioned_or('~'), case_insensitive=True)
client.remove_command("help")

#Starting Defaults

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name="My Talking Angela"))

@client.command()
async def load(ctx, extension):
	if ctx.author.id == ownerid:
		client.load_extension(f'cogs.{extension}')
		await ctx.send(f'{extension} has been loaded!')
	else:
		return False

@client.command()
async def unload(ctx, extension):
	if ctx.author.id == ownerid:
		client.unload_extension(f'cogs.{extension}')
		await ctx.send(f'{extension} has been unloaded!')
	else:
		return False

@client.command()
async def reload(ctx, extension):
	if ctx.author.id == ownerid:
		client.reload_extension(f'cogs.{extension}')
		await ctx.send(f'{extension} has been reloaded!')
	else:
		return False

#Finishing Touch

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

with open('token.txt') as f:
	token = f.read()

client.run(f'{token}')
