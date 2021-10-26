import discord
from settings import Bot_Version
from discord.ext import commands

discordVersion = (discord.__version__)

class Version_Check(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(description="Tells the user the current version of Discord and the bot's current version respectively.")
	async def version(self, ctx):
		# Tells the user the current version of Discord and the bot's current version respectively
		await ctx.send(f'The current Discord version is: {discordVersion}\nThe current Bot version is: {Bot_Version}')

def setup(bot):
	bot.add_cog(Version_Check(bot))