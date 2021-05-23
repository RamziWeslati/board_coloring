class Board:
    """
    A class that represents board of tiles, each having a color

    Attributes
    ----------
    colors: list
        colors listed from highest to lowest ranking
    init_state: list of list of str (colors)
        initital state of board colors per tile
        if init_state is not passed a randomized board is created
    size:    int
        size of board,
        can be infered from init_state

    Methods
    -------
    get_edgy_neighbors():
        gets neighboring tiles to the edge that can get colored
    update_edges(new_color):
        update the edge position with given a new color
    """
    def __init__(self, colors, init_state=None, size=None):
        if (not init_state and not size):
        	raise ValueError('must provide an initital state of colors or a size of a randomized one')

        if (len(colors) == 0):
        	raise ValueError('must provide at least one color')
        self.colors = colors        # colors are ranked by the given order
        if (init_state):
            self.state = init_state
            self.size = len(init_state)
        else:
            from random import choices
            self.state = [choices(colors, k=size) for _ in range(size)]
            self.size = size

        # Edge tiles connected to origin
        self.colored = set()
        self.edges = set()
        self._init_edges()

    def _init_edges(self, current=(0, 0), seen=None):
        """
        determines initial state of the coloring edge

        Parameters
        ----------
        current: tuple: (int, int)
            current tile to consider as an edge
        seen: dp set of seen tiles

        Returns
        -------
        None
        """
        if not seen:
            seen = set()
        if (current not in seen):
            seen.add(current)
            curr_row, curr_column = current
            candidate_edges = self.get_edgy_neighbors(current)

            for candidate in candidate_edges:
                cand_row, cand_column = candidate
                if (self.state[cand_row][cand_column] != self.state[curr_row][curr_column]):
                    if (current not in self.edges): # TODO optimize this not to check twice
                        self.colored.add(current)
                        self.edges.add(current)

                else:
                    self.colored.add(current)
                    self._init_edges(candidate, seen)

    def get_edgy_neighbors(self, tile):
        """
        gets neighboring tiles to the edge that have not yet been colored

        Parameters
        ----------
        tile: tuple: (int, int)
            tile to consider

        Returns
        -------
        edgy_neighbors: list of tuple of int: list(tuple((int, int)))
            list of candidate tiles to color
        """
        neighbors = []
        row, column = tile

        if (column < self.size - 1):  # right neighbor
            neighbors.append((row, column + 1))
        if (column > 0):  # left neighbor
            neighbors.append((row, column - 1))
        if (row < self.size - 1):  # bottom neighbor
            neighbors.append((row + 1, column))
        if (row > 0):  # top neighbor
            neighbors.append((row - 1, column))

        edgy_neighbors = [ neighbor for neighbor in neighbors if neighbor not in self.colored]
        return edgy_neighbors

    def update_edges(self, new_color):
        """
        update the edge position with given a new color

        Parameters
        ----------
        new_color: str
            color to move the edge accordingly

        Returns
        -------
        None
        """
        seen = set()
        old_edges = self.edges.copy()
        for edge in old_edges:
            current_seen = self._update_current_edge(new_color, edge, seen)
            seen.update(current_seen)

    def _update_current_edge(self, new_color, current, seen):
        """
        recursivley updates edge position

        Parameters
        ----------
        new_color: str
            color to move the edge accordingly
		current: tulpe: (int, int)
			tile to consider
		seen: dp set of computed tiles

        Returns
        -------
        seen:
        	considered tiles
        """
        if current not in seen:
            seen.add(current)
            keep_edge, append_edge = False, False
            current_neighbors = self.get_edgy_neighbors(current)
            curr_row, curr_column = current
            curr_color = self.state[curr_row][curr_column]

            for candidate in current_neighbors:
                cand_row, cand_column = candidate
                cand_color = self.state[cand_row][cand_column]

                if (cand_color == new_color):
                    self.colored.add(current)
                    self._update_current_edge(new_color, candidate, seen)
                elif candidate not in self.edges:
                    # current has a neighbor that is not in current edge 
                    # and not with the new color
                    # Add current to edge, if current not an older egde
                    if current not in self.edges:
                        append_edge = True
                    elif cand_color != curr_color:
                        # if older edge, keep as edge
                        keep_edge = True

            if not keep_edge and current in self.edges:
                # if older edge and no longer an edge
                self.edges.remove(current)

            if append_edge:
                # current is a new edge
                self.colored.add(current)
                self.edges.add(current)

            return seen