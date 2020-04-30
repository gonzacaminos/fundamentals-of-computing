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

    # create a game
    twenty48 = twentyfortyeight(HEIGHT,WIDTH)
    
    EXAMPLE_GRID = [[0 + 0 for _dummy_col in range(WIDTH)]
                        for _dummy_row in range(HEIGHT)]    
    # add tests using suite.run_test(....) here
    
    # test the initial configuration of the board using the str method
    suite.run_test(str(twenty48), str(EXAMPLE_GRID), "Test #0: init")

    # report number of tests and failures
    suite.report_results()
