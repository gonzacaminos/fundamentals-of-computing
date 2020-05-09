"""
Merge function for 2048 game.
"""
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

#print merge([2,0,2,4]),    "should return [4,4,0,0]"
#print merge([0,0,2,2]),    "should return [4,0,0,0]"
#print merge([2,2,0,0]),    "should return [4,0,0,0]"
#print merge([2,2,2,2,2]),  "should return [4,4,2,0,0]"
#print merge([8,16,16,8]),  "should return [8,32,8,0]"