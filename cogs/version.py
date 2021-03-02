import discord
from settings import disc_version
from discord.ext import commands

discordVersion = (discord.__version__)

class Version_Check(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(description="Tells the user the current version of Discord and the bot's current version respectively.")
	async def version(self, ctx):
		# Tells the user the current version of Discord and the bot's current version respectively
		await ctx.send(f'The current Discord version is: {discordVersion}\nThe current bot version is: {disc_version}')

def setup(bot):
	bot.add_cog(Version_Check(bot))