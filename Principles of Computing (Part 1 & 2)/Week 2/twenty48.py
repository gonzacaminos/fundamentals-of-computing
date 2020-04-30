"""
Clone of 2048 game.
"""

#import poc_2048_gui
import test_2048 as test_suite
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def next_available(line):
    """
    Finds the next available empty
    (represented by 0) slot
    """
    for next_av in range(len(line)):
        if(line[next_av]==0):
            return next_av
    
def move_to_left(line):
    """
    Moves all the positive numbers 
    to the left replacing the zeroes
    """
    new_line = line[:]
    for num in range(len(line)):
        new_line[num] = 0
        if(line[num] > 0):
            new_line[next_available(new_line)] = line[num]
    return new_line

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = move_to_left(line)

    for tile in range(len(new_line)-1):
        if(new_line[tile] == new_line[tile+1]):
            new_line[tile] *= 2
            new_line[tile+1] = 0 


    new_line = move_to_left(new_line)                 
    
        
    return new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width  = grid_width
        self.grid = []
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 + 0 for _dummy_col in range(self.grid_width)]
                            for _dummy_row in range(self.grid_height)]
        # Add new_tile x 2
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return 0

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return 0

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0
    

twenty48 = TwentyFortyEight(4,6)
test_suite.run_suite(TwentyFortyEight)
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
