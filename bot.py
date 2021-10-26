from settings import AUTH_TOKEN
import discord
from discord.ext import commands

discordVersion = (discord.__version__)

bot = commands.Bot(command_prefix = '!')

# The initial if checks that bot is the one sending the message, and if so will not run the command.  
# This is to prevent the bot being stuck in a loop

# This is the initial startup, giving a visual indicator in the command line that the bot has come online
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

try:
	bot.load_extension('cogs.version')
	bot.test('test')
except commands.errors.ExtensionNotFound as e:
	print(f'No command named: {e.name} found.')

bot.run(AUTH_TOKEN)