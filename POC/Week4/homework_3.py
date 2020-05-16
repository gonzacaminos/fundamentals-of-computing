"""
Homework 3
"""

import math

def permutList(_list):
    if not _list:
            return [[]]
    res = []
    _list = list
    for e in _list:
            temp = _list[:]
            temp.remove(e)
            res.extend([[e] + r for r in permutList(temp)])

    return res

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
                print new_seq
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans


def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)


def compute_expected_value_2():
    """
    Function to compute expected value of simple dice game with 
    four possibilities
    """
    outcomes = set([1, 2, 3, 4])
    seqs = list(gen_all_sequences(outcomes, 2))

    expected_value = 0

    for _idx, _seq in enumerate(seqs):
        expected_value += _seq[0] * _seq[1]

    # We divide the total on the number of sequences we have
    return expected_value


def count_consecutives(r_list):
    """
    Counts the number of consecutive values on a list
    Returns False if found non consecutives
    """
    count = 1
    # Avoid IndexError for  random_list[i+1]
    for i in range(len(r_list) - 1):
        # Check if the next number is consecutive
        # by checking the absolute number of the difference
        if (abs(r_list[i] - r_list[i+1]) == 1):
            count += 1
        else:
            return False
    return True


def compute_probability_3(_num_choices, _list_len, percent=False):
    """
    Function to compute probability of generating consecutive numbers
    {1 .. 10}
    """
    if(_list_len > _num_choices):
        return "Impossible to return a consecutive list, num of choices < list length"
    outcomes = set([_x for _x in range(0, _num_choices)])
    #seqs = list(gen_all_sequences(outcomes, _list_len))
    seqs = list(gen_all_sequences(outcomes, _list_len))
    #perms = permutList(outcomes)
    
    print seqs[0], seqs[1]
    #print len(seqs), math.factorial(_num_choices) / math.factorial(_num_choices - _list_len)
    consecutives = 0

    for _idx, _seq in enumerate(seqs):
        if(len(_seq) == len(set(_seq)) and count_consecutives(_seq)):

            #print _seq, count_consecutives(_seq)
            consecutives += 1

    if(percent):
        # We divide the total on the number of sequences we have
        return float(consecutives) / len(seqs)

    return consecutives


def richie_theorem(_num_choices, _list_len):
    """
    The Richie Theorem it's a solution a friend, Richie,
    came up with while braining this problem. Probably this
    solution has existed for 2000 years but we're happy
    thinking we invented it.
    _num_choices represents the amount of consecutives values, {0,9} is 10, etc

    """
    if(_list_len > _num_choices):
        return "Impossible to return a consecutive list, num of choices < list length"
    return abs(_num_choices - _list_len + 1) * 2


length = 5
numbers = 10

# prob = math.factorial(5 + 10) /
#print "Exercise 2, expected value:", compute_expected_value_2()
#test_list_2 = [0, 1, 2, 3, 4]
#print "Exercise 3, number of probabilities:", compute_probability_3()
print "Exercise 3, percent of probabilities:", compute_probability_3(10,5,True)
#print "Exercise 3, Richie Theorem:", richie_theorem(10, test_list_2)
