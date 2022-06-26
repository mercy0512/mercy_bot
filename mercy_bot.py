import discord
from discord.ext import commands

bot = commands.bot(commands_prefix= '!')

@bot.event
async def on_ready():
    print('>> bot is  online <<')

bot.run(OTkwNDYyMTU5NDAwMDgzNTU3.GzpelO.PSo5LLn1sYO0uaSMvTnxysLS3li5Sv6P408ETs)