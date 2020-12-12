# TODO: #1
# Encode a 2048_game.Game2048State, use onehot encoding
# Will be called by get_batch
# return a tensor
def encode(state):
    return
    
# TODO: #2
# Generate training data for NN
# Needs to call encode function to encode state
# return: (input, output)
# input: list of encoded states
# output: list of correspond utilities
def get_batch(board_size, num_games):
    return

# TODO: #3
# Generate training data file
# Call get_batch function, save training data as a ".pkl" file
if __name__ == "__main__":
    print()