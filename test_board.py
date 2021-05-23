from .board import Board

test_case_0 = {
		'colors': ['blue', 'red', 'black'],
		'init_state': [
						['blue', 'red', 'black'],
						['red', 'red', 'black'],
						['red', 'red', 'black'],
					],
		'expected_init_edge': {(0, 0)},
		'expected_red_update_edge': {(0, 1), (1, 1), (2, 1)},
}

test_case_1 = {
	'colors': ['blue', 'red', 'black'],
	'init_state': [
					['blue', 'red', 'black'],
					['blue', 'blue', 'black'],
					['blue', 'red', 'black'],
				],
	'expected_init_edge': {(0, 0), (1, 1), (2, 0)},
	'expected_black_update_edge': {(0, 0), (2, 0), (1, 1), (2, 2), (0, 2)},  # all neighbor tiles to red tiles
	'expected_red_update_edge': {(0, 1), (1, 1), (2, 1)},
}

test_case_2 = {
	'colors': ['blue', 'red', 'black'],
	'init_state': [
					['blue', 'blue', 'blue'],
					['blue', 'blue', 'blue'],
					['blue', 'blue', 'black'],
				],
	'expected_init_edge': {(1, 2), (2, 1)},
	'expected_black_update_edge': set()
}

def test_edges_init():
	"""tests edges tiles detection at init"""
	board_0 = Board(test_case_0['colors'], test_case_0['init_state'])
	board_1 = Board(test_case_1['colors'], test_case_1['init_state'])
	board_2 = Board(test_case_2['colors'], test_case_2['init_state'])

	assert board_0.edges == test_case_0['expected_init_edge']
	assert board_1.edges == test_case_1['expected_init_edge']
	assert board_2.edges == test_case_2['expected_init_edge']


def test_edges_update():
	"""test egde expension with new color"""
	board_0 = Board(test_case_0['colors'], test_case_0['init_state'])
	board_1_red = Board(test_case_1['colors'], test_case_1['init_state'])
	board_1_black = Board(test_case_1['colors'], test_case_1['init_state'])
	board_2 = Board(test_case_2['colors'], test_case_2['init_state'])
	
	board_0.update_edges('red')
	board_1_red.update_edges('red')
	board_1_black.update_edges('black')
	board_2.update_edges('black')

	assert board_0.edges == test_case_0['expected_red_update_edge']
	assert board_1_red.edges == test_case_1['expected_red_update_edge']
	assert board_1_black.edges == test_case_1['expected_black_update_edge']
	assert board_2.edges == test_case_2['expected_black_update_edge']
