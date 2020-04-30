"""
Clone of 2048 game.
"""

#import poc_2048_gui
import test_2048 as test_suite
import random
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
        self.DIRECTION = {UP:   self.traverse_grid((0, 0), (0, 1), self.grid_width),
                          LEFT: self.traverse_grid((0,0), (1,0), self.grid_height),
                          DOWN: self.traverse_grid((self.grid_height-1,0), (0,1), self.grid_width),
                          RIGHT:self.traverse_grid((0,self.grid_width-1), (1,0), self.grid_height)}

        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 + 0 for _dummy_col in range(self.grid_width)]
                            for _dummy_row in range(self.grid_height)]
        self.new_tile()
        self.new_tile()

        return self.grid
    
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
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width
    def traverse_grid(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction
        
        Both start_cell is a tuple(row, col) denoting the
        starting cell
        
        direction is a tuple that contains difference between
        consecutive cells in the traversal

        Returns a list with the processed grid cells
        """
        _processed_grid = []
        _values = []
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            _processed_grid.append([row,col])
            
         
        return _processed_grid

    def get_grid_values(self, start_cell, direction, num_steps): 
        """
        Function that iterates on the grid on a linear direction
        Gets the value of each tile and returns a list
        Uses the same parameters that the traverse_grid method
        """
        _grid = self.traverse_grid(start_cell,direction, num_steps)
        _values = []
        for _dummy_x in _grid:
            _value = self.get_tile(_dummy_x[0],_dummy_x[1])
            _values.append(_value)
        return _values

    def set_grid_values(self, start_cell, direction, num_steps, list): 
        """
        Function that iterates on the grid on a linear direction
        Sets the value of each tile and returns a list
        Uses the same parameters that the traverse_grid method
        """
        _grid = self.traverse_grid(start_cell,direction, num_steps)
        for _index, _value in enumerate(_grid):
            #print list[_index], _value[0], _value[1]
            self.set_tile(_value[0],_value[1], list[_index])

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        print "MOVING >>>"
        _this_direction = self.DIRECTION[direction]
        _offset = OFFSETS[direction]
        _steps =  self.grid_height  if direction == UP or direction == DOWN else self.grid_width 

        for _dummy_x in _this_direction:
            _temp_list = self.get_grid_values(_dummy_x,_offset, _steps) # Gets the grid values
            _temp_list = merge(_temp_list) # Merges the column/row
            self.set_grid_values(_dummy_x,_offset, _steps, _temp_list) # Sets the values to the merged list 

    
    def print_grid_snapshot(self):
         print "SNAPSHOT:"
         for row in range(self.grid_height):
            print self.grid[row]

    def get_empty_cells(self):
        _cells = []
        for _row in range(self.grid_height):
            for _col in range(self.grid_width):
                if(self.grid[_row][_col] == 0):
                    _cells.append([_row,_col])
                   
        return _cells

    def get_random_empty_cell(self):
        _cells = self.get_empty_cells()
        if(self.get_empty_cells()):
            return random.choice(_cells)
        else:
            return False

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        _number = 2 if random.random() < .9 else 4
        _empty_cell = self.get_random_empty_cell()
        
        if(_empty_cell):
            self.set_tile(_empty_cell[0],_empty_cell[1],_number)    
        else: 
            return "No more empty"     

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]
    

#twenty48 = TwentyFortyEight(4,6)
test_suite.run_suite(TwentyFortyEight)
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
