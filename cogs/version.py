import discord
from settings import disc_version
from discord.ext import commands

discordVersion = (discord.__version__)

class version(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def on_message(self, bot):
		if message.content.startswith('!version'):
			await message.channel.send(f'The current Discord version is: {discordVersion}\nThe current bot version is: {disc_version}') # This is an f-string.  It parses the string to look for expressions (namely, discordVersion)

def setup(bot):
	bot.add_cog(version(bot))