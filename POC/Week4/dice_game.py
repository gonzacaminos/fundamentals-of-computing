"""
Analyzing a simple dice game
"""


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

def max_repeats(seq):
    """
    Compute the maximum number of times that an outcome is repeated
    in a sequence
    """
    max_value = 0

    for i,v in enumerate(seq):
        max_value = max(max_value,seq.count(v))
     
    return max_value


def compute_expected_value():
    """
    Function to compute expected value of simple dice game.
    Gets all the possible sequences on the dice outcomes
    and calculates what will be the result if playing all
    the possibilities.
    """
    outcomes = set([1, 2, 3, 4, 5, 6])
    seqs = list(gen_all_sequences(outcomes, 3))
    expected_value = 0
    
    for i, _seq in enumerate(seqs):
        max_rep = max_repeats(_seq)
        if (max_rep == 2):
            expected_value += 10
        elif(max_rep == 3):
            expected_value += 200
            
    # We divide the total on the number of sequences we have
    return expected_value/float(len(seqs))


def run_test():
    """
    Testing code, note that the initial cost of playing the game
    has been subtracted
    """
    outcomes = set([1, 2, 3, 4, 5, 6])
    print "All possible sequences of three dice are"
    print gen_all_sequences(outcomes, 3)
    print
    print "Test for max repeats"
    print "Max repeat for (3, 1, 2) is", max_repeats((3, 1, 2))
    print "Max repeat for (3, 3, 2) is", max_repeats((3, 3, 2))
    print "Max repeat for (3, 3, 3) is", max_repeats((3, 3, 3))
    print
    print "Ignoring the initial $10, the expected value was $", compute_expected_value()
    
run_test()
