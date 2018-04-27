import numpy as np
from numpy.random import rand


class NeuralNetwork:
    def __init__(self, n_inputs, n_hidden=None, n_outputs=1):
        self.n_inputs = n_inputs
        self.n_hidden = n_hidden
        self.n_outputs = n_outputs

        if n_hidden is None:
            self.W = rand(n_outputs, n_inputs)
        else:
            self.W1 = rand(n_hidden, n_inputs)

    def predict(self, input):
        return self.W @ np.array(input)

