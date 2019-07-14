import numpy as np

from learning.SupervisedNetwork import NeuralNetwork

if __name__ == '__main__':
    nn = NeuralNetwork(10, 1)

    assert nn.n_inputs == 10
    assert nn.n_outputs == 1
    print(nn.W, nn.W.shape)
    assert nn.predict([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert nn.predict([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == np.dot(nn.W, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
