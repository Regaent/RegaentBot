import discord
from settings import disc_version
from discord.ext import commands

class disc_cmds(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def cmds(self, message):
		if message.author == client.user:
			return
		if message.content.startswith('!help'):
			await message.channel.send('Bot Commands:\n''!version - Posts current discord and bot version.')

def setup(bot):
	bot.add_cog(disc_cmds(bot))