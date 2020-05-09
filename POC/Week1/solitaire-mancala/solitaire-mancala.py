"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]

    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = configuration[:]

    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return str(self._board[::-1])

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for _dummy_x in self._board[1:len(self._board) + 1]:
            if (_dummy_x > 0):
                return False

        return True

    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if (house_num == 0):
            return False
        return self.get_num_seeds(house_num) == house_num

    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if (self.is_legal_move(house_num)):
            self._board[house_num] = 0
            for _dummy_house_num in range(house_num - 1, -1, -1):
                self._board[_dummy_house_num] = self._board[_dummy_house_num] + 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for _dummy_house_num in range(1, len(self._board)):
            if (self.is_legal_move(_dummy_house_num)):
                return _dummy_house_num

        return 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """

        test_game = SolitaireMancala() 
        test_game.set_board(self._board)
        moves = []

        while (test_game.choose_move() != 0):
            
            next_move = test_game.choose_move()
            moves.append(next_move)
            test_game.apply_move(next_move)

        return moves 


# Create tests to check the correctness of your code


def test_mancala():
    """
    Test code for Solitaire Mancala
    """

    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"

    config1 = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(config1)
    pre_game = str(my_game)
    print "Testing plan_moves - Computed:", my_game.plan_moves()
    print "Testing set_board - Computed:", pre_game, "Expected:", str(
        [0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(
        1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(
        3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(
        5), "Expected:", config1[5]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(
        4), "Expected:", config1[4]
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(
        5), "Expected: True"
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(
        4), "Expected: False"
    print "Testing apply_move - Computed:", my_game.apply_move(5)

    plan = my_game.plan_moves()

    for _x in plan[:len(plan)+1]:
        """ 
        Wins the game 
        """
        my_game.apply_move(_x)

    print "Testing set_board - Computed:", pre_game, " ", str(my_game)
    print "Testing is_game_won:", my_game.is_game_won()


test_mancala()

# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())
