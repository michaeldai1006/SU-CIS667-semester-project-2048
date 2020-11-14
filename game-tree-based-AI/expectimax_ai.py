# Import game state, action and player class, random module
Game2048State = __import__('2048_game').Game2048State
Game2048Action = __import__('2048_game').Game2048Action
Game2048Player = __import__('2048_game').Game2048Player
import random
import math
import numpy as np

# Max searching depth
search_max_depth = 4

# Processed tree nodes
processed_nodes = 0

# Tree search node class
class Node(object):
    def __init__(self, state, player):
        self.state = state
        self.player = player

    # Calculate utility of state
    def getUtility(self):
        utility = 0

        # Sum non 0 tile values, times factor
        # factor = log2(tile)
        for i in range(self.state.board.shape[0]):
            for j in range(self.state.board.shape[1]):
                if self.state.board[i][j] != 0:
                    utility += self.state.board[i][j] * math.log(self.state.board[i][j], 2)

        return utility

# Find next state using expectimax search
def getNextState(state):
    # Reset processed nodes counter
    global processed_nodes
    processed_nodes = 0

    # Find next best move    
    next_node = expectimax(Node(state, Game2048Player.USER), 0)

    # Next state result and number of processed tree nodes
    return next_node.state

# Expectimax tree search
def expectimax(node, depth):
    # Increase tree node counter
    global processed_nodes
    processed_nodes += 1

    # Max depth reached
    if depth == search_max_depth: return node

    if node.player == Game2048Player.USER: return findMax(node, depth)
    if node.player == Game2048Player.GAME: return findExp(node, depth)

# Find max state
def findMax(node, depth):
    # Best next move
    next_node = None

    # List all possible next nodes
    next_nodes = []
    valid_actions = node.state.validActions()
    for action in valid_actions:
        if (action == Game2048Action.SLIDE_UP):
            next_state = node.state.slideUp()
            next_nodes.append(Node(next_state, Game2048Player.GAME))
        elif (action == Game2048Action.SLIDE_DOWN):
            next_state = node.state.slideDown()
            next_nodes.append(Node(next_state, Game2048Player.GAME))
        elif (action == Game2048Action.SLIDE_LEFT):
            next_state = node.state.slideLeft()
            next_nodes.append(Node(next_state, Game2048Player.GAME))
        elif (action == Game2048Action.SLIDE_RIGHT):
            next_state = node.state.slideRight()
            next_nodes.append(Node(next_state, Game2048Player.GAME))
        elif (action == Game2048Action.ROTATE_CW):
            next_state = node.state.rotateCenterCW()
            next_nodes.append(Node(next_state, Game2048Player.GAME))
        elif (action == Game2048Action.ROTATE_CCW):
            next_state = node.state.rotateCenterCCW()
            next_nodes.append(Node(next_state, Game2048Player.GAME))
    
    # Find optimal board
    for node in next_nodes:
        if next_node == None: next_node = node
        elif node.getUtility() > expectimax(node, depth + 1).getUtility(): next_node = node
    
    # Next move
    if next_node == None: return node
    else: return next_node

# Find expected state
def findExp(node, depth):
    # Expected next move
    next_node = None

    # All possible next nodes
    next_nodes = []

    # Add all possible next nodes with new tile value of 2
    for i in range(node.state.board.shape[0]):
        for j in range(node.state.board.shape[1]):
            if (node.state.board[i][j] == 0):
                next_state = Game2048State(node.state.size)
                next_state.board = np.copy(node.state.board)
                next_state.board[i][j] = 2
                next_nodes.append(Node(next_state, Game2048Player.USER))

    # Add all possible next nodes with new tile value of 4
    for i in range(node.state.board.shape[0]):
        for j in range(node.state.board.shape[1]):
            if (node.state.board[i][j] == 0):
                next_state = Game2048State(node.state.size)
                next_state.board = np.copy(node.state.board)
                next_state.board[i][j] = 4
                next_nodes.append(Node(next_state, Game2048Player.USER))

    # Find next expected node
    for node in next_nodes:
        if next_node == None: next_node = node
        elif node.getUtility() < expectimax(node, depth + 1).getUtility(): next_node = node
    
    # Next move
    if next_node == None: return node
    else: return next_node

if __name__ == "__main__":
    # AI demo
    state = Game2048State(4)
    state = state.initialState()
    print(state)

    for _ in range(0, 50000):
        state = getNextState(state)
        print("Number of tree nodes processed: %d" % processed_nodes)
        print(state)
        state = state.addNewTile()
        print()
        print()
        print(state)