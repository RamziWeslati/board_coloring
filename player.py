class Player:
    """
    A class that represents an entity that solves board coloring in a greedy manner

    Attributes
    ----------
    board: Board
        initialized board to play on

    Methods
    -------
    play():
        solves the board colring game by continuously updating edges
    """
    def __init__(self, board):
        """
        Constructs all the necessary attributes for the Player object

        Parameters
        ----------
        board: Board
            board to:
             keep track of current edges
             get possible colors and their ranks
             get uncolored tiles neighboring the current edge
             update edge position given a new color
        """
        self.board = board

    def _choose_color(self):
        """
        chooses color resulting in the largest number of tiles connected to origin

        Parameters
        ----------
        None

        Returns
        -------
        return color with best ranking if tied in number of connected tiles
        """
        from collections import Counter

        counted = set()
        edgy_color_count = Counter()
        for edge in self.board.edges:
            edgy_neighbors = self.board.get_edgy_neighbors(edge)
            for neighbor in edgy_neighbors:
                n_row, n_col = neighbor
                if neighbor not in counted:
                    edgy_neighbor_color = self.board.state[n_row][n_col]
                    edgy_color_count[edgy_neighbor_color] += 1
                    counted.add(neighbor)

        # return greediest color with best rank
        max_color = max(edgy_color_count)
        max_count = edgy_color_count[max_color]
        color_rank = self.board.colors.index(max_color)
        for color, count in edgy_color_count.items():
            candidate_rank = self.board.colors.index(color)
            if count == max_count and candidate_rank < color_rank: # highest rank, same n_edges
                color_rank = candidate_rank
                max_color = color

        return max_color

    def play(self):
        """
        solves the board while keeping track of player moves

        Parameters
        ----------
        None

        Returns
        -------
        return 
        moves: list
            sequence of colors leading to a win in a greedy manner
        """
        moves = []
        while(self.board.edges):        # keeping coloring until we have no more edges
            next_color = self._choose_color()
            # record player moves
            moves.append(next_color)
            # no need for counter as len is O(1) in python
            print(f'My move number {len(moves)} would be to chose the color {next_color}')
            # update board edges with new color
            self.board.update_edges(next_color)

        print(f'Ha! I won in {len(moves)} moves')
        return moves
