Game2048State = __import__('2048_game').Game2048State
Game2048Action = __import__('2048_game').Game2048Action
Game2048Player = __import__('2048_game').Game2048Player
BaselineAI = __import__('baseline_ai')
ExpectimaxAI = __import__('expectimax_ai')

import math

# Calculate utility of state
def getUtility(state):
    utility = 0
    empty_count = 0

    # Sum non 0 tile values, times factor
    # factor = log2(tile)
    # Count num of zero tiles
    for i in range(state.board.shape[0]):
        for j in range(state.board.shape[1]):
            if state.board[i][j] != 0:
                utility += state.board[i][j] * math.log(state.board[i][j], 2)
            else:
                empty_count += 1

    # More zero tiles = higher utility
    utility += empty_count * 5

    return utility

if __name__ == "__main__":
    # AI demo
    state = Game2048State(8)
    state = state.initialState()
    print(state)

    for _ in range(0, 50000):
        state = ExpectimaxAI.getNextState(state)
        # state = BaselineAI.getNextState(state)
        print(state)
        if (state.isGameEnded()[0] == True): print(getUtility(state)); break

        state = state.addNewTile()
        print(state)
        if (state.isGameEnded()[0] == True): print(getUtility(state)); break