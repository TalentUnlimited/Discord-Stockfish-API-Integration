from stockfish import Stockfish

stockfish = Stockfish(path="stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe")

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