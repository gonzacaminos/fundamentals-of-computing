"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import tictactoe_board as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10000  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player

# Add your functions here.


def mc_trial(board, player):
    """
    Plays a trial game alternating the players
    """
    _player = player
    while(board.check_win() == None):
        _square = random.choice(board.get_empty_squares())    
        board.move(_square[0], _square[1], _player)   
        _player = provided.switch_player(_player)
    #print board.check_win()


def mc_update_scores(scores, board, player):
    """
    Updates the scores grids by scoring a given board and a given player
    """
    #board.check_win()
    if(board.check_win() == provided.DRAW):
        scores = create_empty_sq_list(len(scores))
        return scores

    _score_current = SCORE_CURRENT * 1 if board.check_win() == player else SCORE_CURRENT * -1
    _score_other = SCORE_OTHER * 1 if board.check_win() is not player else SCORE_OTHER * -1

    #print board.check_win(), player, _score_current, _score_other

    for _sq_x in range(len(scores)):
        for _sq_y in range(len(scores[_sq_x])):
            #print board.square(_sq_x ,_sq_y)
            if(board.square(_sq_x ,_sq_y) == player):
                scores[_sq_x][_sq_y] += _score_current
            elif(board.square(_sq_x ,_sq_y) is not 1):
                # If it's not empty
                scores[_sq_x][_sq_y] += _score_other
    

def get_best_move(board, scores):
    """
    Gets the best possible move for a given board by using a scores grid
    """
    _empty_sq = board.get_empty_squares()
    _max_value = 0
    _best_move = ()
    if(len(_empty_sq) > 0):
        for _dumm_sq in _empty_sq:
            _sq_score = scores[_dumm_sq[0]][_dumm_sq[1]]
            if(_sq_score > _max_value):
                _max_value = _sq_score
                _best_move = _dumm_sq
    return _best_move

def create_empty_sq_list(dimension):
    """
    Create an empty (filled with zeroes) square list 
    """
    return [([0] * dimension) for i in range(dimension)]

def mc_move(board, player, trials):
    """
    Run a Monte Carlo test  and makes the best possible move with the given player
    """
    _scores =  create_empty_sq_list(board.get_dim()) # Empty scores list

    for _dummy in range(trials):
        _board = board.clone() # New board based on the given board
        mc_trial(_board,player)
        mc_update_scores(_scores, _board,player)
        

    return get_best_move(board, _scores)
   




# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
