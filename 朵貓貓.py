import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'Bot is ready')



bot.run('MTAwOTMzNjM1OTkyNTg1MDIyMw.Gg1JlG.7Ernb_aD0Rd45qqwkI9PkiiS9Hf2DrPvgmmYEk')

