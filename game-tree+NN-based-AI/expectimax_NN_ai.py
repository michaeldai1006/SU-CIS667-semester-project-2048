# Import game state, action and player class, random module
Game2048State = __import__('2048_game').Game2048State
Game2048Action = __import__('2048_game').Game2048Action
Game2048Player = __import__('2048_game').Game2048Player
import random
import math
import numpy as np
import torch as tr
from torch.nn import Sequential, Conv2d, Linear, Flatten, LeakyReLU, Tanh, Bilinear, AlphaDropout

# Max searching depth
search_max_depth = 0

# Processed tree nodes
processed_nodes = 0

### HW4 COPY
def BlockusNet1(board_size):
    net = Sequential(
        Flatten(),
        AlphaDropout(p=0.01, inplace=True),
        Linear(in_features=board_size*board_size,out_features=10, bias = True)
    )
    return net

def calculate_loss(net, x, y_targ):
    y = net(x)
    loss = tr.sum((y - y_targ)**2)
    return y, loss

def optimization_step(optimizer, net, x, y_targ):
    optimizer.zero_grad()
    y, loss = calculate_loss(net, x , y_targ)
    loss.backward()
    optimizer.step()
    return y, loss

####

# TODO: #4
# Generate NN module
# return type: torch.nn.Module
def getNet():
    return

# TODO: #5
# Estimates utility of node
# Takes a instance of Node class as input, estimate its utility using NN module generate by function getNet
# return: estimated utility, type int
def nn_utility(node):
    return

# Tree search node class
class Node(object):
    def __init__(self, state, player):
        self.state = state
        self.player = player

    # TODO: #6
    # Calculate utility of state
    # Modify this function, so it adds the return value of nn_utility to the utility result
    def getUtility(self):
        utility = 0
        empty_count = 0

        # Sum non 0 tile values, times factor
        # factor = log2(tile)
        # Count num of zero tiles
        for i in range(self.state.board.shape[0]):
            for j in range(self.state.board.shape[1]):
                if self.state.board[i][j] != 0:
                    utility += self.state.board[i][j] * math.log(self.state.board[i][j], 2)
                else:
                    empty_count += 1

        # More zero tiles = higher utility
        utility += empty_count * 5

        return utility

# Find next state using expectimax search
def getNextState(state):
    # Reset processed nodes counter
    global processed_nodes
    processed_nodes = 0

    # Update search depth
    depth_map = {2: 5, 4: 2, 6: 2, 8: 1, 10: 1}
    global search_max_depth
    search_max_depth = depth_map[state.size]

    # Find next best move    
    next_node = expectimax(Node(state, Game2048Player.USER), 0)

    # Next state result and number of processed tree nodes
    return next_node.state

# Expectimax tree search
def expectimax(node, depth):
    # Increase tree node counter
    global processed_nodes
    processed_nodes += 1

    # Max or Exp the node
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
    max_utility = float('-inf')
    for n in next_nodes:
        expected_utility = expectimax(n, depth + 1)
        if (expected_utility > max_utility): next_node = n; max_utility = expected_utility
    
    # Next move
    if next_node == None: return node
    else: return next_node

# Find expected state
def findExp(node, depth):
    if depth >= search_max_depth: return node.getUtility()

    # Expected utility
    expected_utility = 0.0

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

    # Sum up expected utility
    for n in next_nodes:
        expected_utility += 1/len(next_nodes) * expectimax(n, depth + 1).getUtility()
    
    # Expected utility result
    return expected_utility

if __name__ == "__main__":
#### HW4
    board_size = 4
    net = BlockusNet1(board_size=board_size)

    import pickle as pk
    with open("data%d.pkl" % board_size,"rb") as f: (x, y_targ) = pk.load(f)

    # Optimization loop
    optimizer = tr.optim.Adam(net.parameters())
    train_loss, test_loss = [], []
    shuffle = np.random.permutation(range(len(x)))
    split = 10
    train, test = shuffle[:-split], shuffle[-split:]

    for epoch in range(5000):
        y_train, e_train = optimization_step(optimizer, net, x[train], y_targ[train])
        y_test, e_test = calculate_loss(net, x[test], y_targ[test])
        if epoch % 10 == 0: print("%d: %f (%f)" % (epoch, e_train.item(), e_test.item()))
        train_loss.append(e_train.item() / (len(shuffle)-split))
        test_loss.append(e_test.item() / split)
    
    tr.save(net.state_dict(), "model%d.pth" % board_size)
    
    import matplotlib.pyplot as pt
    pt.plot(train_loss,'b-')
    pt.plot(test_loss,'r-')
    pt.legend(["Train","Test"])
    pt.xlabel("Iteration")
    pt.ylabel("Average Loss")
    pt.show()
    
    pt.plot(y_train.detach().numpy(), y_targ[train].detach().numpy(),'bo')
    pt.plot(y_test.detach().numpy(), y_targ[test].detach().numpy(),'ro')
    pt.legend(["Train","Test"])
    pt.xlabel("Actual output")
    pt.ylabel("Target output")
    pt.show()
