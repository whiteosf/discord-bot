import os
from dotenv import load_dotenv

import random

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name}")

@bot.command(name="Sacrifice", help="Sacrifice stuff")
async def sacrifice(ctx, x):
    opt = ["Yummy", "Nom", "Thank you", "*screeching*", "Mort is thankful", "I need more", "Scrumptious", "UWU"]
    await ctx.send(opt[random.randint(0, 7)])
    
bot.run(TOKEN)
 #random stuff

