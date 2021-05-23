from .player import Player
from .board import Board

test_case_0 = {
		'colors': ['blue', 'red', 'black'],
		'init_state': [
						['blue', 'red', 'black'],
						['red', 'red', 'black'],
						['red', 'red', 'black'],
					],
		'expected_n_moves': 2,
		'expected_sequence_to_win': ['red', 'black'],
}


def test_play():
	board_0 = Board(test_case_0['colors'], test_case_0['init_state'])

	player_0 = Player(board_0)

	moves_0 = player_0.play()

	assert moves_0 == test_case_0['expected_sequence_to_win']
