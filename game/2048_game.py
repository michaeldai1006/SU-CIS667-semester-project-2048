"""
2048 game file
2048 game state, game operations and interactive game entry point
Students: tdai06, kkha, dyzheng, ztanruan
"""

"""
Packages
"""
import numpy as np
from enum import Enum

"""
Enum that indicates different players of the game
GAME - player game
USER - player user
"""
class Game2048Player(Enum):
    GAME = 'game'
    USER = 'user'

"""
Enum that indicates different actions available to player
"""
class Game2048Action(Enum):
    SLIDE_UP = 1
    SLIDE_DOWN = 2
    SLIDE_LEFT = 3
    SLIDE_RIGHT = 4
    ROTATE_CW = 5
    ROTATE_CCW = 6

"""
Represents current game state and available game operations
"""
class Game2048State(object):
    """
    Init game board with size
    """
    def __init__(self, size):
        # Game board size
        self.size = size

        # Empty game board, 0 indicates a empty tile
        self.board = np.empty((size, size),dtype=np.int)
        self.board[:] = 0

    """
    Return a string representation of the current game board
    """
    def __str__(self):
        # TODO: 1
        return ""

    """
    Initialize game, generate 2 new tiles with value of either 2 or 4 at random locations
    Return a new game state instance instead of modify the current game state
    """
    def initialState(self):
        # TODO: 2
        return

    """
    Add a new tile at a random empty spot with value of either 2 or 4
    Return a new game state instance instead of modify the current game state
    """
    def addNewTile(self):
        # TODO: 3
        return 

    """
    Slide the tiles up, merge tiles if needed
    Return a new game state instance instead of modify the current game state
    """
    def slideUp(self):
        # TODO: 4
        return

    """
    Slide the tiles down, merge tiles if needed
    Return a new game state instance instead of modify the current game state
    """
    def slideDown(self):
        # TODO: 5
        return

    """
    Slide the tiles toward left, merge tiles if needed
    Return a new game state instance instead of modify the current game state
    """
    def slideLeft(self):
        # TODO: 6
        return

    """
    Slide the tiles toward right, merge tiles if needed
    Return a new game state instance instead of modify the current game state
    """
    def slideRight(self):
        # TODO: 7
        return
    
    """
    Rotate the center 2x2 square clockwise for 90 degrees
    Return a new game state instance instead of modify the current game state
    """
    def rotateCenterCW(self):
        # TODO: 8
        return

    """
    Rotate the center 2x2 square counterclockwise for 90 degrees
    Return a new game state instance instead of modify the current game state
    """
    def rotateCenterCCW(self):
        # TODO: 9
        return
    
    """
    Return a list of valid actions
    Example: [Game2048Action.SLIDE_UP, Game2048Action.ROTATE_CW, Game2048Action.ROTATE_CCW]
    """
    def validActions(self):
        # TODO: 10
        return

    """
    Check whether current game is ended and find the winner
    return (True, Game2048Player.USER) if tile with value 2048 appears
    return (True, Game2048Player.GAME) if no matter how user rotates the center 2x2 square there are no more than 2 valid actions
    return (False,) if game continues
    """
    def isGameEnded(self):
        # TODO: 11
        return

"""
Interactive game entry game
Prompt the user to play the game
"""    
if __name__ == "__main__":
    # TODO: 12
    print("Hello, World!")