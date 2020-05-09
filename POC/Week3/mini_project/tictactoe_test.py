"""
Template testing suite for Tic Tac Toe
"""

import poc_simpletest

def run_suite(tictactoe):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite() 

    # create a game
    ttt = tictactoe()
    
    suite.run_test(str(twenty48), str(EXAMPLE_GRID), "Test #0: init")
    
    suite.report_results()
