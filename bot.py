import discord
from discord.ext import commands
from main import *
from emojis_ids import emojis_ids

with open("token.txt", "r") as f:
	TOKEN = (f.read())

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='-', intents=intents)


square_w_or_b = {

}
s = "b"
for letter_ in range(8):
	for number in range(8):
		letter = chr(ord('a') + letter_)
		number = number+1
		
		if s == "b":
			square_w_or_b[letter+str(number)] = "b"
			s = "w"
		elif s == "w":
			square_w_or_b[letter+str(number)] = "w"
			s = "b"
	
	if s == "b":
		s = "w"
	elif s == "w":
		s = "b"

Empty_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

def convertFEN(FEN):
	FEN=(FEN.split(" "))[0]+"/"

	fen_l = []
	tmp = []

	if FEN != []:
		for x in FEN:
			if x == '/':
				fen_l.append(tmp)
				tmp = []
			else:
				if x.isnumeric():
					for x in range(int(x)):
						tmp.append('e')
				else:
					if x.isupper() == 1:
						tmp.append(f'w{x.lower()}')
					else:
						tmp.append(f'b{x}')

	emojis = []

	for row in range(len(fen_l)):
		for square in range(len(fen_l[row])):
			#print(f"{chr(ord("h") - (square))}{8-row}-{fen_l[row][square]}")
			if (fen_l[row][square])=="e":
				emojis.append(f"<:{fen_l[row][square]}{square_w_or_b[(chr(ord('a') + (square)))+str(8-row)]}s:{emojis_ids[fen_l[row][square]+square_w_or_b[(chr(ord('a') + (square)))+str(8-row)]+'s']}>")
			else:
				emojis.append(f"<:{fen_l[row][square]}{square_w_or_b[(chr(ord('a') + (square)))+str(8-row)]}:{emojis_ids[fen_l[row][square]+square_w_or_b[(chr(ord('a') + (square)))+str(8-row)]]}>")
		emojis.append(f" {str(8-row)}\n")

	for x in range(8):
		emojis.append(f"  {chr(ord('a') + (x))}  ") 

	return "".join(emojis)

#print(convertFEN(Empty_FEN))


@bot.command()
async def new(ctx):
	stockfish.set_fen_position(Empty_FEN)
	embed = discord.Embed(title="Chess Board", description=convertFEN(Empty_FEN), color=0X3483eb)
	await ctx.send(embed=embed)

@bot.command()
async def move(ctx, arg):
	make_move(arg)
	embed = discord.Embed(title="Chess Board", description=convertFEN(stockfish.get_fen_position()), color=0X3483eb)
	await ctx.send(embed=embed)

	make_move(get_best_move())
	embed = discord.Embed(title="Chess Board", description=convertFEN(stockfish.get_fen_position()), color=0X34eb52)
	await ctx.send(embed=embed)

bot.run(TOKEN)