"""
Template testing suite for probability and combinatorics
"""

import poc_simpletest
import homework_3 as comb

def run_suite():
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite() 

    #print "Exercise 2, expected value:", comb.compute_expected_value_2()
    suite.run_test(comb.compute_probability_3(10,5), comb.richie_theorem(10, 5), "Test #0: List to 5, 10 choices.")
    suite.run_test(comb.compute_probability_3(8,5), comb.richie_theorem(8, 5), "Test #1: List to 5, 8 choices.")
    suite.run_test(comb.compute_probability_3(7,5), comb.richie_theorem(7, 5), "Test #2: List to 5, 7 choices.")
    suite.run_test(comb.compute_probability_3(5,5), comb.richie_theorem(5, 5), "Test #3: List to 5, 5 choices.")

    #suite.run_test(comb.compute_probability_3(5,10), comb.richie_theorem(5, 10), "Test #1: List to 5, 10 choices.")
    #suite.run_test(comb.compute_probability_3(15,10), comb.richie_theorem(15, 10), "Test #2: List to 15, 10 choices.")

    suite.report_results()

run_suite()