# Rock-paper-scissors-lizard-Spock mini-project

import random 

def name_to_number(name):
    
  
    if name == "rock":
        number = 0
        
    elif name == "Spock":
        number =1
        
    elif name == "paper":
        number = 2
        
    elif name == "lizard":
        number = 3
        
    elif name == "scissors":
        number = 4
    
    else:
        number = "Incorrect element name"
        
    return number    
    

def number_to_name(number):
  
    if number == 0:
        name = "rock"
        
    elif number == 1:
        name = "Spock"
    
    elif number == 2:
        name = "paper"
    
    elif number == 3:
        name = "lizard"
    
    elif number == 4:
        name = "scissors"
        
    else: 
        name = "Incorrect number"
        
    return name  
    
      

def rpsls(player_choice): 
   
    print "" 
    
    print "Player chooses " + player_choice

    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0,5)
    
    comp_choice = number_to_name(comp_number)
    
    print "Computer chooses " + comp_choice
    
    winner_number = (comp_number - player_number) % 5
    
    if (winner_number == 1) or (winner_number == 2):
        print "Computer wins!"
        
    elif (winner_number == 3) or (winner_number == 4):
        print "Player wins!"
    
    else:
        print "Player and computer tie!"

        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



