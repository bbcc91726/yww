import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'Bot is ready')



bot.run('MTAwOTMzNjM1OTkyNTg1MDIyMw.GpKmqU.gJEUQuwD-NB5Wgt9OEWui4_1_uKYFjZDpjkYY0')

