import os
from dotenv import load_dotenv

import random

import discord
from discord.ext import commands

import math

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='!')

@bot.listen()
async def on_ready1():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name}")

@bot.command(name = "equ", help="Solves your sacrifised quadratic and linear equations, takes in three arguments: a, b, c, which are coefficients. Even if coefficient is 0, it has to be listed. As example for equation 3x-4=0 you have to send 0 3 -4 as argumants.")
async def equation(ctx, a, b, c):
    if a==0:
        await ctx.send(f"{ctx.author.display_name}, equation: x = {(-c)/b}")
    elif a!=0:
        discr= b**2 - 4*a*c
        sqr = square_root_simplifier(discr)
        if discr>=0:
            num = math.sqrt(discr)
            if isinstance(num, int)==True:
                await ctx.send(f"{ctx.author.display_name}, equation: x = {-b+num/2*a} ,  {-b-num/2*a}")
            elif isinstance(num, int)==False:
                await ctx.send(f"{ctx.author.display_name}, equation: x = -({b} ± √{discr})/{2*a} ")
        else:
            if sqr[0]==1:
                await ctx.send(f"{ctx.author.display_name}, equation: x = ({-b} ± i√{discr})/{2*a}")
            else:
                await ctx.send(f"{ctx.author.display_name}, equation: x = ({-b} ± {sqr[0]}i√{sqr[1]})/{2*a}")
    elif a==0 & b==0:
        await ctx.send(f"{ctx.author.display_name}, equation: There is no x to solve for")

@bot.command(name = "sqrt_simplifier", help = "Simplifies square roots, takes in radicand as argument.")
async def sqrt_simplifier(ctx, radicand):
    ans = square_root_simplifier(radicand)
    if radicand>0:
        await ctx.send(f"{ctx.author.display_name} sqrt simplifier: {ans[0]}√{ans[1]}")
    elif radicand == 0:
        await ctx.send("0")
    else:
        await ctx.send(f"{ctx.author.display_name}, sqrt simplifier: {ans[0]}i√{ans[1]}")
        


@bot.command(name = "plot", help = "")
async def plot(ctx, *args, x):
    args=[*args]
    answr=0
    degree = len(args)-1
    if x==0:
        answr=args[-1]
    elif x==1:
        answr=sum(args)
    else:
        for i in range(0, degree+1):
            answr+= args[i]*x**degree
            degree-=1
    await ctx.send(f"{ctx.author.display_name}, plot: y = {answr}")


@bot.command(name="Sacrifice", help="Sacrifice stuff")
async def sacrifice(ctx, *args):
    opt = ["Yummy", "Nom", "Thank you", "*screeching*", "Mort is thankful", "I need more", "Scrumptious", "UWU"]
    await ctx.send(opt[random.randint(0, 7)])

@bot.command(name="Backstory", help="Just type this command to learn the lore behind Mort")
async def backstory(ctx):
    await ctx.send("Long ago, in the very center of the Earth, a single rock of magma and hot gases combined with an unseen power, creating an ominpotent being of mass-destruction. Feared by all, the beast was contained in an ancient form of hydroflask by the first VSCO girls. They worshipped the being from the hydroflask for centuries, until a tourist accidentally opened the bottle. The beast arose from it's prison of plastic, taking form. The beast began it's destructive course. After decades of hiding, a single human was able to tame the beast. Over time, it developed a body to control, that of a small lemur. The body allowed the beast to communicate with humans. The being was further tamed to solve mathematical equations and now spends it's days solving the problems of any humans that give sacrifices. He likes discord and spends most of his time there, where he set up a service for helping humans with math. The creature was Mort.")

@bot.command(name="Power", help="Input a number and the exponent (in that order) and Mort returns the answer")
async def power(ctx, a, y):
    await ctx.send(f"{ctx.author.display_name}, power: {a**y}")

@bot.command(name = "linear_systems", help="Solves linear systems of equations in the form of y = ax + b and y = cx + d. Enter the a, b, c, and d of the equations.")
async def linear_systems(ctx, a, b, c, d):    
    x = (d-b)/(a-c)    
    y = (a*x)+b    
    await ctx.send(f"Your x value is equal to {x} and your y value is equal to {y}")
    
@bot.command("add_subtract", help = "takes values that you want to add and subtract. eg. putting in 12, -10, 1 would give you 3.")
async def add_and_subtract(ctx, *args):
    await ctx.send(sum(*args))
    
@bot.command(name = "multiply", help= "multiplies two values")
async def multiply(ctx, x,y):
    await ctx.send(x*y)

@bot.command(name = "divide", help = "divides two values")
async def divide(ctx, x,y):
    await ctx.send(x/y)



def perfect_squares_generator(n):
    s = 2
    while n>s**2:
        yield s**2
        s+=1
def square_root_simplifier(radicand):
    coefficient = 1
    n = perfect_squares_generator(radicand/2)
    try:
        s = next(n)
        while s<radicand/2:
            while radicand%s==0:
                radicand/=s
                coefficient*=math.sqrt(s)
            s = next(n)
    except StopIteration:
        pass
    return [int(coefficient), int(radicand)]

bot.run(TOKEN)

