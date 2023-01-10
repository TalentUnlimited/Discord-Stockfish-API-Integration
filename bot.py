import discord
from discord.ext import commands
from main import *

with open("token.txt", "r") as f:
	TOKEN = (f.read())

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='.', intents=intents)


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

"""
square = "d2"
piece = (stockfish.get_what_is_on_square(square))
if piece==None:
	piecestr = f"e{square_w_or_b[square]}s"
else:
	piece = piece.name.split("_")
	piecestr = piece[0][0] + ("n" if piece[1]=="KNIGHT" else piece[1][0] if piece[1]!="KNIGHT" else "") + square_w_or_b[square]

#print(piecestr.lower())
"""

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

	for row in range(len(fen_l)):
		for square in range(len(fen_l[row])):
			print(f'{chr(ord("h") - (square))}{8-row}-{fen_l[row][square]}')

	return fen_l

print(convertFEN(Empty_FEN))


@bot.command()
async def new(ctx):
	stockfish.set_fen_position(Empty_FEN)
	embed = discord.Embed(title="Chess Board", description="<:this:470903994118832130>", color=0X3483eb)
	await ctx.send(embed=embed)

bot.run(TOKEN)


