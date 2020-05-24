"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""
import random, poc_simpletest


def next_available(line):
    """
    Finds the next available empty
    (represented by 0) slot
    """
    for next_av in range(len(line)):
        if(line[next_av] == 0):
            return next_av

def next_available2(line):
    """
    Finds the next available empty
    (represented by 0) slot
    """
    for next_av in range(len(line)-1):
        if(line[next_av] == 0):
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

def merge2(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = move_to_left(line)

    for tile in range(len(new_line)-1):
        if(new_line[tile] == new_line[tile+1]):
            new_line[tile] *= 2
            new_line[tile-1] = 0

    new_line = move_to_left(new_line)

    return new_line

def merge3(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = move_to_left(line)

    for tile in range(len(new_line)-1):
        if(new_line[tile] == new_line[tile-1]):
            new_line[tile] *= 2
            new_line[tile+1] = 0

    new_line = move_to_left(new_line)

    return new_line

def merge4(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = line[:]
    for num in range(len(line)):
        new_line[num] = 0
        if(line[num] > 0):
            new_line[next_available2(new_line)] = line[num]

    for tile in range(len(new_line)-1):
        if(new_line[tile] == new_line[tile+1]):
            new_line[tile] *= 2


    new_line = move_to_left(new_line)

    return new_line

def merge5(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = line[:]
    for num in range(len(line)):
        new_line[num] = 0
        if(line[num] > 0):
            new_line[next_available2(new_line)] = line[num]

    for tile in range(len(new_line)-1):
        if(new_line[tile] == new_line[tile+1]):
            new_line[tile] += new_line[tile-1]
            new_line[tile+1] = 0


    new_line = move_to_left(new_line)

    return new_line

def merge6(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = line[:]
    for num in range(len(line)):
        new_line[num] = 0
        if(line[num] > 0):
            new_line[next_available2(new_line)] = line[num]

    for tile in range(len(new_line)-1):
        if(new_line[tile] == new_line[tile+1]):
            new_line[tile] += new_line[tile]
            new_line[tile-1] = 0


    new_line = move_to_left(new_line)

    return new_line

def merge7(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = line[:]
    for num in range(len(line)):
        new_line[num] = 0
        if(line[num] > 0):
            new_line[next_available(new_line)] = line[num]

    for tile in range(len(new_line)-2):
        if(new_line[tile] == new_line[tile-1]):
            new_line[tile] += 2
            new_line[tile-1] = 0


    new_line = move_to_left(new_line)

    return new_line

def merge8(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = line[:]
    for num in range(len(line)):
        new_line[num] = 0
        if(line[num] > 0):
            new_line[next_available(new_line)] = line[num]

    for tile in range(len(new_line)-2):
        if(new_line[tile] == new_line[tile-1]):
            new_line[tile-1] *= 2
            new_line[tile-1] = 0


    new_line = move_to_left(new_line)

    return new_line

# Create tests to check the correctness of your code
def add_list(_list):
    total = 0
    for i in _list:
        total += i
    return total

def test_2048():
    """
    Test code for Solitaire Mancala
    """

    suite = poc_simpletest.TestSuite() 
  

    bad_things = set()
    num_tests = 50
    file = open('testfile.txt','a') 

    for _test_x in range(num_tests):
        config = [0]
        size = random.randrange(1,11,1)
        choices = [0, 2, 4, 8, 16, 32, 64, 128, 256]

        for _i in range(1,size):
            #config.append(static)
            config.append( random.choice(choices) )

        merged = merge(config) 
        merged2 = merge7(config) 

        

        

        suite.run_test(add_list(merged2),  add_list(merged), "Test #"+str(_test_x) +": Testing merge")
        if (add_list(merged2) != add_list(merged)):
            bad_things.add(tuple(config))
            file.write(str(tuple(config)) + '\n') 

            
    suite.report_results()
    #print len(bad_things), "Failed tests,"
    print bad_things, len(bad_things)
 
    file.close() 

    


test_2048()

def Log2(x): 
    if x == 0: 
        return False
  
    return (math.log10(x) / 
            math.log10(2)); 
  
# Function to check 
# if x is power of 2 
def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == 
            math.floor(Log2(n))); 

TEST_CASES = [ [16, 128, 0, 64, 128, 128, 2, 0, 256],[0, 2, 16, 128, 128, 32],[0, 256, 64, 64, 256, 16, 16, 4, 16, 256], [4, 4, 4, 4, 0, 128], [0, 2, 8, 8, 64, 4, 4, 2], [0, 64, 0, 64, 2, 16, 256], [32, 2, 8, 2, 32, 64, 2, 2, 16, 2], [2,0,2,0,0,2], [128, 128, 16, 16, 0, 1028, 2, 2, 32],[0, 8, 8, 16, 64, 4, 8, 16], [0, 2, 2, 0, 8, 8, 256, 0, 4] ]


for i in TEST_CASES:
    print len(i)
# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())
