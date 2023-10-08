import discord
from discord.ext import commands
import time

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def ping(ctx):
    starting_time = time.time()
    msg = await ctx.send("Calculating...")
    ending_time = time.time()
    ping_time = (ending_time - starting_time) * 1000
    await msg.edit(content=f"The ping is: {ping_time:.2f}ms")

@bot.command()
async def credits(ctx):
    msg = "CREDITS:\n"
    
    with open("assets/CREDITS.txt", "r") as file:
        credits = file.readlines()

    for line in credits:
        if line.startswith("#"):
            pass #comment
        else:
            msg = msg + line + "\n"

    await ctx.send(msg)

if __name__ == "__main__":
    bot.run("")
