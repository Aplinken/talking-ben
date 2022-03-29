import discord
from discord.ext import commands
import os

# Client created
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=commands.when_mentioned_or('~'), case_insensitive=True)
client.remove_command("help")

# Starting Defaults

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name="My Talking Angela"))

@commands.is_owner()
@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'{extension} has been loaded!')

@commands.is_owner()
@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	await ctx.send(f'{extension} has been unloaded!')

@commands.is_owner()
@client.command()
async def reload(ctx, extension):
	client.reload_extension(f'cogs.{extension}')
	await ctx.send(f'{extension} has been reloaded!')

# Finishing Touch

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

token = os.environ.get('TOKEN')
client.run(token)
