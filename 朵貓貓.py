import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'Bot is ready')



bot.run('MTAwOTMzNjM1OTkyNTg1MDIyMw.GeRtnu.xRp5fIhfWcV93Peav-Hf1mRf_-l54b8z9YeZmc')

