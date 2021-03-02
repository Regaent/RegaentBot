from settings import AUTH_TOKEN
from discord.ext import commands
import discord
from settings import disc_version
discordVersion = (discord.__version__)

# Intents allow specific features of discordpy to be enabled or disabled to prevent certain events from triggering/being sent
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client()

# The initial if checks that bot is the one sending the message, and if so will not run the command.  
# This is to prevent the bot being stuck in a loop

# This is the initial startup, giving a visual indicator in the command line that the bot has come online
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
    	return

	if message.content.startswith('!version'):
		await message.channel.send(f'The current Discord version is: {discordVersion}\nThe current bot version is: {disc_version}') # This is an f-string.  It parses the string to look for expressions (namely, discordVersion)

# try:
# 	bot.load_extension('cogs.Help_Commands')
# except commands.errors.ExtensionNotFound as e:
# 	print(f'No command named: {e.name} found.')

client.run(AUTH_TOKEN)