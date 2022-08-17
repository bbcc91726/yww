import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'Bot is ready')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(890071214356324424)
    await channel.send(f'{mamber} join!')
    


bot.run('MTAwOTMzNjM1OTkyNTg1MDIyMw.Gf40yH.D-pSBYo66rhyc5ZMoWR2nnuajFTPDriPsJDBX4')

