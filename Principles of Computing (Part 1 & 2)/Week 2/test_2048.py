"""
Template testing suite for Solitaire Mancala
"""

import poc_simpletest

def run_suite(twentyfortyeight):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite() 
    
    HEIGHT = 4 
    WIDTH = 6
    NUM_CELLS = HEIGHT*WIDTH
    DIR_UP = str([[0,0], [0,1], [0,2], [0,3], [0,4], [0,5]])
    DIR_LEFT = str([[0,0], [1,0], [2,0], [3,0]])
    DIR_DOWN = str([[3,0], [3,1], [3,2], [3,3], [3,4], [3,5]])
    DIR_RIGHT = str([[0,5], [1,5], [2,5], [3,5]])

    # Directions, DO NOT MODIFY
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    # create a game
    twenty48 = twentyfortyeight(HEIGHT,WIDTH)
    
    EXAMPLE_GRID = [[0 + 0 for _dummy_col in range(WIDTH)]
                        for _dummy_row in range(HEIGHT)]    
    # add tests using suite.run_test(....) here
    
    # test the initial configuration of the board using the str method
    suite.run_test(str(twenty48), str(EXAMPLE_GRID), "Test #0: init")
    twenty48.new_tile()
    #suite.run_test(str(twenty48.get_tile(1,1)), str(4), "Test #1: set/get_tile")
    twenty48.new_tile()
    #suite.run_test(str(twenty48.get_tile(3,3)), str(2), "Test #1: set/get_tile")
    suite.run_test(str(len(twenty48.get_empty_cells())), str(NUM_CELLS -4), "Test #2: get_empty_cells") # Should return NUM_CELLS - 2 
    #twenty48.set_tile(2,3, 2)
    twenty48.new_tile()
    suite.run_test(str(len(twenty48.get_empty_cells())), str(NUM_CELLS -5), "Test #2: get_empty_cells") # Should return NUM_CELLS - 3 
    #suite.run_test(str(twenty48.get_random_empty_cell()), str("Random"), "Test #3: get_random_empty_cell") 
    suite.run_test(str(twenty48.DIRECTION[UP]), DIR_UP, "Test #4: UP direction") 
    suite.run_test(str(twenty48.DIRECTION[LEFT]), DIR_LEFT, "Test #4: LEFT direction") 
    suite.run_test(str(twenty48.DIRECTION[DOWN]), DIR_DOWN, "Test #4: DOWN direction") 
    suite.run_test(str(twenty48.DIRECTION[RIGHT]), DIR_RIGHT, "Test #4: RIGHT direction") 
    twenty48.print_grid_snapshot()
    suite.run_test(str(twenty48.move(UP)), "Something", "Test #5: Move Up") 
    twenty48.print_grid_snapshot()
    suite.run_test(str(twenty48.move(DOWN)), "Something", "Test #5: Move Down") 
    twenty48.print_grid_snapshot()
    suite.run_test(str(twenty48.move(LEFT)), "Something", "Test #5: Move Left") 
    twenty48.print_grid_snapshot()


    suite.run_test(str(twenty48.reset()), str(twenty48), "Test #4: reset") 

    #for _dummy_i in range(22):
    #    print twenty48.new_tile()
    
    #suite.run_test(str(twenty48), str(EXAMPLE_GRID), "Test #0: init")

    # report number of tests and failures
    suite.report_results()
