import discord
from settings import bot_version
from discord.ext import commands

class help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == client.user:
			return
		if message.content.startswith('!help'):
			await message.channel.send('Bot Commands:\n''!version - Posts current discord and bot version.')

def setup(bot):
	bot.add_cog(help(bot))