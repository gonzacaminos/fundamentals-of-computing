# Testing template for "Guess the number"

###################################################
# Student should add code for "Guess the number" here



import simplegui
import random
import math

#global variables

secret_number = 0
game_range = 100
number_of_guesses = 7


# helper function to start and restart the game

def new_game():
    
    # initialize global variables used in your code here
  
    global number_of_guesses
    
    if game_range == 100:
        number_of_guesses = 7
    else:
        number_of_guesses = 10

    print ""
    print "New" , game_range, "game, have fun!"
    print "Number of remaining guesses is", number_of_guesses
    print ""  
        
    global secret_number
    secret_number = random.randrange(0,game_range)

# define event handlers for control panel
def range100():
    
    # button that changes the range to [0,100) and starts a new game 
   
    global game_range
    game_range = 100
    new_game()

def range1000():
    global game_range
    game_range = 1000    
    new_game()
    
def input_guess(guess):
    
    global number_of_guesses
    number_of_guesses -= 1
    
    # main game logic goes here	
    if number_of_guesses < 0:
        print ""
        print "You lose, try again"
        new_game()
    else:
        print "Number of remaining guesses is", number_of_guesses
        print ""
        
        guess = int(guess)
        print "Guess was" , guess

        if guess < secret_number :
            print "Higher"

        elif guess > secret_number:
            print "Lower"

        else: 
            print "Correct"

    
# create frame

frame = simplegui.create_frame("Canvas", 500,500)
frame.add_input("Guess number", input_guess, 100)
frame.add_button("Range100", range100, 100)
frame.add_button("Range1000", range1000, 100)

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric




###################################################
# Start our test #1 - assume global variable secret_number
# is the the "secret number" - change name if necessary


###################################################
# Output from test #1
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Higher!
#
#Guess was 75
#Number of remaining guesses is 5
#Lower!
#
#Guess was 62
#Number of remaining guesses is 4
#Higher!
#
#Guess was 68
#Number of remaining guesses is 3
#Higher!
#
#Guess was 71
#Number of remaining guesses is 2
#Higher!
#
#Guess was 73
#Number of remaining guesses is 1
#Higher!
#
#Guess was 74
#Number of remaining guesses is 0
#Correct!
#
#New game. Range is from 0 to 100
#Number of remaining guesses is 7

###################################################
# Start our test #2 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#range1000()
#secret_number = 375	
#input_guess("500")
#input_guess("250")
#input_guess("375")

###################################################
# Output from test #2
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#New game. Range is from 0 to 1000
#Number of remaining guesses is 10
#
#Guess was 500
#Number of remaining guesses is 9
#Lower!
#
#Guess was 250
#Number of remaining guesses is 8
#Higher!
#
#Guess was 375
#Number of remaining guesses is 7
#Correct!
#
#New game. Range is from 0 to 1000
#Number of remaining guesses is 10



###################################################
# Start our test #3 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#secret_number = 28	
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")

###################################################
# Output from test #3
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Lower!
#
#Guess was 50
#Number of remaining guesses is 5
#Lower!
#
#Guess was 50
#Number of remaining guesses is 4
#Lower!
#
#Guess was 50
#Number of remaining guesses is 3
#Lower!
#
#Guess was 50
#Number of remaining guesses is 2
#Lower!
#
#Guess was 50
#Number of remaining guesses is 1
#Lower!
#
#Guess was 50
#Number of remaining guesses is 0
#You ran out of guesses.  The number was 28
#
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
