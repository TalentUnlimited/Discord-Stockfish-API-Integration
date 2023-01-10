from stockfish import Stockfish

stockfish = Stockfish(path="stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe", depth=18)

def make_move(move):
	moves = [move]
	stockfish.make_moves_from_current_position(moves)

def get_best_move():
	return stockfish.get_best_move()

"""
Testing
make_move("e2e4")
print(stockfish.get_board_visual())
make_move(get_best_move())
print(stockfish.get_board_visual())
make_move("g1f3")
print(stockfish.get_board_visual())
make_move(get_best_move())
print(stockfish.get_board_visual())
"""

"""
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

square = "d2"
piece = (stockfish.get_what_is_on_square(square))
if piece==None:
	piecestr = f"e{square_w_or_b[square]}s"
else:
	piece = piece.name.split("_")
	piecestr = piece[0][0] + ("n" if piece[1]=="KNIGHT" else piece[1][0] if piece[1]!="KNIGHT" else "") + square_w_or_b[square]

#print(piecestr.lower())
"""