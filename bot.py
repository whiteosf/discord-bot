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
async def sacrifice(ctx, args):
    opt = ["Yummy", "Nom", "Thank you", "*screeching*", "Mort is thankful", "I need more", "Scrumptious", "UWU"]
    await ctx.send(opt[random.randint(0, 7)])

@bot.command(name="Backstory", help="Just type this command to learn the lore behind Mort")
async def backstory(ctx):
    await ctx.send("Long ago, in the very center of the Earth, a single rock of magma and hot gases combined with an unseen power, creating an ominpotent being of mass-destruction. Feared by all, the beast was contained in an ancient form of hydroflask by the first VSCO girls. They worshipped the being from the hydroflask for centuries, until a tourist accidentally opened the bottle. The beast arose from it's prison of plastic, taking form. The beast began it's destructive course. After decades of hiding, a single human was able to tame the beast. Over time, it developed a body to control, that of a small lemur. The body allowed the beast to communicate with humans. The being was further tamed to solve mathematical equations and now spends it's days solving the problems of any humans that give sacrifices. He likes discord and spends most of his time there, where he set up a service for helping humans with math. The creature was Mort.")

@bot.command(name="Power", help="Input a number and the exponent (in that order) and Mort returns the answer")
async def power(ctx, a, y):
    await ctx.send(a**y)

bot.run(TOK)

