from player import Player
from board import Board

if __name__ == '__main__':
	board = Board(['red', 'black', 'yellow'], size=3)
	player = Player(board)

	player.play()