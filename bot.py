import discord
from discord.ext import commands

with open("token.txt", "r") as f:
	TOKEN = (f.read())

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command()
async def new(ctx):
	embed = discord.Embed(title="Chess Board", description="<:wkw:1062064746989371582>", color=0X3483eb)
	await ctx.send(embed=embed)

bot.run(TOKEN)


