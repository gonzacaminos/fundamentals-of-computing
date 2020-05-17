"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
#import codeskulptor
# codeskulptor.set_timeout(20)



def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return sorted(set(sorted_sequences))


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """

    count = [x * hand.count(x) for x in set(hand)]
    return max(count)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    _dice_values = [x for x in range(1, num_die_sides+1)]
    _seq = gen_sorted_sequences(_dice_values, num_free_dice)
    _expected_value = 0

    for _idx, _roll in enumerate(_seq):
        _dices = held_dice + _roll
        #print _dices, score(_dices)
        _expected_value += score(_dices)
    
    return _expected_value / float(len(_seq))

def gen_permutations(outcomes, length):
    """
    Iterative function that permutates the set of all sequences of
    outcomes of given length
    """

    perm = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in perm:
            for item in outcomes:
                new_seq = list(seq)
                if item not in new_seq:
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        perm = temp
    return perm


def gen_combinations(outcomes, length):
    """
    Function that creates all sorted sequences via gen_permutations
    """
    all_sequences = gen_permutations(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
        
    _seq = []
    _hand_len = len(hand)
    for _x in range(0, _hand_len+1, 1):
        _seq += gen_combinations(hand[_x:],_hand_len-_x)
    print "Hand:", hand, "Subsets", _seq
    return set( _seq )


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    return (0.0, ())


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score


#run_example()


#import poc_holds_testsuite
# poc_holds_testsuite.run_suite(gen_all_holds)

