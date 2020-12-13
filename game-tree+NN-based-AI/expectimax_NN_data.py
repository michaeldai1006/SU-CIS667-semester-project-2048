# TODO: #1
# Encode a 2048_game.Game2048State, use onehot encoding
# Will be called by get_batch
# return a tensor
def encode(state):
    onehot = tr.zeros((3, state.size, state.size))
    for i in state.plays[1]:
        onehot[1, i[0]:i[0]+i[2].shape[0], i[1]:i[1]+i[2].shape[1]] = tr.Tensor(i[2].copy())
    for i in state.plays[2]:
        onehot[2, i[0]:i[0]+i[2].shape[0], i[1]:i[1]+i[2].shape[1]] = tr.Tensor(i[2].copy())
    onehot[0,:,:] = ((onehot[1,:,:] + onehot[2,:,:]) == 0).int()
    
    return onehot
    
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
