"""
Template testing suite for probability and combinatorics
"""

import poc_simpletest
import miniproject_yahtzee as yahtzee
import test_gen_all_holds as test_holds
def run_suite():
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite() 
    hand = (1, 1, 1, 5, 6)

    gen_seq = yahtzee.gen_sorted_sequences((1,2,3,4,5,6),2)
    suite.run_test(gen_seq, gen_seq, "Test #0: Gen all sequences.")

    suite.run_test(str(yahtzee.score((1, 1, 1, 5, 6))), "6", "Test #1: Test Scoring.")
    suite.run_test(str(yahtzee.score((6,2,2,2,2))), "8", "Test #2: Test Scoring.")
    suite.run_test(str(yahtzee.score((6,6,6,2,2))), "18", "Test #3: Test Scoring.")
    suite.run_test(str(yahtzee.score((5,6,5,4,1))), "10", "Test #4: Test Scoring.")
    suite.run_test(str(yahtzee.score((1,1,1,4,1))), "4", "Test #5: Test Scoring.")
    suite.run_test(str(yahtzee.score((1,1,1,2,3))), "3", "Test #6: Test Scoring.")
    print
    # Considering I hold a tuple of two dices (2,3), 1 more to roll
    suite.run_test(str( yahtzee.expected_value((2,3), 6, 3)), "3", "Test #7: Test Expected value.")
    suite.run_test(str( yahtzee.expected_value((5,3), 6, 3)), "3", "Test #8: Test Expected value.")
    suite.run_test(str( yahtzee.expected_value((1,1), 6, 3)), "3", "Test #8: Test Expected value.")
    suite.run_test(str( yahtzee.expected_value((1,2), 6, 3)), "3", "Test #8: Test Expected value.")
    print
    suite.run_test(str( yahtzee.strategy((1,1,1,2,3), 6)), "3", "Test #10: Test Strategy.")
    suite.run_test(str( yahtzee.strategy((5,6,5,4,1), 6)), "3", "Test #10: Test Strategy.")

    #suite.run_test(str( yahtzee.gen_all_holds( (1,2) ) ), "3", "Test #9: Test Gen holds.")
    #suite.run_test(str( len(yahtzee.gen_all_holds( (1,6,4) )) ), str( pow(2,len((1,6,4) ) )), "Test #9: Test Gen holds.")

    #suite.run_test(str( yahtzee.gen_all_holds( (1,2,3,4) ) ), "3", "Test #9: Test Gen holds.")

    suite.report_results()

run_suite()

#test_holds.run_suite(yahtzee.gen_all_holds)