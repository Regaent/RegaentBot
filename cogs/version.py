import discord
from settings import bot_version
from discord.ext import commands

discordVersion = (discord.__version__)

class version(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.content.startswith('!version'):
			await message.channel.send(f'The current Discord version is: {discordVersion}\nThe current bot version is: {bot_version}') # This is an f-string.  It parses the string to look for expressions (namely, discordVersion)
			return

def setup(bot):
	bot.add_cog(version(bot))