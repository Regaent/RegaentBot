from settings import AUTH_TOKEN
from discord.ext import commands
import discord
from cogs import version
from cogs import bot_commands

# Intents allow specific features of discordpy to be enabled or disabled to prevent certain events from triggering/being sent
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = discord.ext.commands.Bot(command_prefix='!')

client = discord.Client()

# The initial if checks that bot is the one sending the message, and if so will not run the command.  
# This is to prevent the bot being stuck in a loop
@client.event
async def on_message(message):
    if message.author == client.user:
    	return

# This is the initial startup, giving a visual indicator in the command line that the bot has come online
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

try:
	bot.load_extension('cogs.version')
	bot.load_extension('cogs.bot_commands')
except commands.errors.ExtensionNotFound as e:
	print(f'No command named: {e.name} found.')

client.run(AUTH_TOKEN)