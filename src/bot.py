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

if __name__ == "__main__":
    bot.run("")
