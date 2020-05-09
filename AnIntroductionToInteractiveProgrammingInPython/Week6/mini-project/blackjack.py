# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    
blackjack_img = simplegui.load_image("https://www.dropbox.com/s/pe4m2sycn5nep4x/BLACK.png?dl=1")

# initialize some useful global variables
in_play = False
outcome = "Welcome! Press Deal to start"
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        
        self.hand = []
        
    def __str__(self):
        
        hand = ""
         
                       
        for i in range(0,len(self.hand)):
            hand += str(self.hand[i])
            hand += " "
            
        return "Hand contains " + hand
    
    def reset(self):
        self.hand = []
        
    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        hand_value = 0
        aces = False 
        
        for i in range(0,len(self.hand)):
            
            hand_value += int( VALUES[ self.hand[i].get_rank() ] )
        
            if 'A' == self.hand[i].get_rank():

                    aces = True            

        if aces == False:
                
                return hand_value 
        else: 
            
            if hand_value +10 <= 21:
                return hand_value + 10

            else:
                return hand_value    
                
    
    def draw(self, canvas, pos):         
            for i in range(0,len(self.hand)):
                self.hand[i].draw(canvas, (pos[0]+72*i, pos[1]))
            
            
# define deck class 
class Deck:
    def __init__(self):
        
        self.deck = []
        
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))


    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        #new_deck = list(self.deck)
        return self.deck.pop(0)
    
    def __str__(self):
         
        deck = ""
                                
        for i in range(0,len(self.deck)):
            deck += str(self.deck[i])
            deck += " "
            
        return "Deck contains " + deck
    
player_hand = Hand()
dealer_hand = Hand()
deck = Deck()

#define event handlers for buttons
def deal():
    
    global outcome, in_play, player_hand,score
    outcome = "Hit or Stand?"
    deck.shuffle()
    player_hand.reset()
    dealer_hand.reset()
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    if in_play:
        outcome = "You lost! Hit or Stand?"
        in_play = False
        score -= 1
        
    if player_hand.get_value() == 21 and dealer_hand.get_value() != 21:
        outcome = "You win! New deal?"
        in_play = False
        score += 1

    elif player_hand.get_value() != 21 and dealer_hand.get_value() == 21:
        outcome = "Dealer wins! New deal?"
        in_play = False
        score -= 1

    elif player_hand.get_value() == 21 and dealer_hand.get_value() == 21:
        outcome = "Dealer wins! New deal?"
        in_play = False    
        score -= 1

    else:
        in_play = True
    
    print "Player", player_hand, "Dealer", dealer_hand
    print player_hand.get_value(), dealer_hand.get_value()
    
def hit():
    global outcome, score, in_play
    
    if in_play:
        player_hand.add_card(deck.deal_card())
        
        if player_hand.get_value() > 21:
            in_play = False
            outcome = "You're busted! New deal?"
            score -= 1

        elif player_hand.get_value() == 21:
             score += 1
            
    print "Player", player_hand, "Dealer", dealer_hand
    print player_hand.get_value()
    print dealer_hand.get_value()

   
def stand():
    global outcome, score, in_play

    if player_hand.get_value() > 21:
        in_play = False
        outcome = "You're busted! New deal?"
        
    else:
        
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        
        if dealer_hand.get_value() > 21:
            in_play = False
            outcome = "Dealer Busted! New deal?"
            score += 1
            
        else:
            if dealer_hand.get_value() >= player_hand.get_value():
                in_play = False
                outcome = "Dealer Wins! New deal?"
                score -= 1
                
            else:
                
                in_play = False
                outcome = "You Win! New deal?"
                score += 1                      
   
    print "Player", player_hand, "Dealer", dealer_hand
    print player_hand.get_value()
    print dealer_hand.get_value()

# draw handler    
def draw(canvas):
    
    canvas.draw_polygon([[0, 550], [0, 600], [600, 600], [600, 550]], 12, 'Black', 'Black')    
    canvas.draw_image(blackjack_img, (275/2,275/2), (275,275), [300,280], (275,275))
    canvas.draw_text("Score: " + str(score), (480,580), 22, "White", "sans-serif")
    canvas.draw_text(outcome, (20,580), 22, "White", "sans-serif")
    player_hand.draw(canvas, (220,380))
    dealer_hand.draw(canvas, (220,120))
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [256,168], CARD_BACK_SIZE)

    
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric