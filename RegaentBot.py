import discord
bot_version = '1.0.0.0' # Major.Minor.Release.Build

# Intents allow specific features of discordpy to be enabled or disabled to prevent certain events from triggering/being sent
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

# To load the virtual environment source bot-env/bin/activate
# Dotenv does not work with virtual environment.  
#import dotenv
#from dotenv import load_dotenv
#load_dotenv()

import os
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

# Logging is for writing to a file called discord.log, rather than outputting the results to the console
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

# This is the initial startup, giving a visual indicator in the command line that the bot has come online
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# The initial if checks that bot is the one sending the message, and if so will not run the command.  
# This is to prevent the bot being stuck in a loop
@client.event
async def on_message(message):
    if message.author == client.user:
      	return

# If the above is not effective, the bot will read the user message and respond with the appropriate outcome.
    if message.content.startswith('$version'):
    	discordVersion = (discord.__version__)
    	await message.channel.send(f'The current Discord version is: {discordVersion}\nThe current bot version is: {bot_version}') # This is an f-string.  It parses the string to look for expressions (namely, discordVersion)

client.run('NzMwNjg2MDM4ODA4NDYxMzQz.XwbGZw.DFcfQH4VtGA91C-jAa9el83Vbjs')