import csv
import numpy as np
from keras import models, layers, losses, optimizers, activations


class ImitationNetwork:
    N_INPUTS = 26
    N_HIDDEN = 50
    N_OUTPUTS = 4

    def __init__(self, name):
        self.name = 'imitation_network'

        self.model = models.Sequential()
        alpha = 0.01  # LeakyRelu alpha

        self.model.add(layers.Dense(self.N_INPUTS, activation=activations.linear))
        self.model.add(layers.LeakyReLU(alpha))

        self.model.add(layers.Dense(self.N_HIDDEN, activation=activations.linear))
        self.model.add(layers.LeakyReLU(alpha))

        self.model.add(layers.Dense(self.N_OUTPUTS, activation=activations.sigmoid))

        self.model.compile(optimizer=optimizers.Adam(), loss=losses.mean_squared_error)

    def fit(self, file_name):
        num_epochs = 30000  # number of epochs for training
        input_file = open(file_name, 'r')
        rows = csv.reader(input_file)
        inputs = []
        outputs = []
        for row in rows:
            inputs.append(row[1:26])
            outputs.append(row[26:30])

        inputs = np.matrix(inputs)
        outputs = np.matrix(outputs)
        history = self.model.fit(inputs, outputs, batch_size=inputs.size, epochs=num_epochs)
        self.save()

    def load(self):
        """
        Loads the neural network's weights from disk.

        :param name: model's name.
        :type name: str.
        """
        self.model.load_weights(self.name)

    def save(self):
        """
        Saves the neural network's weights to disk.

        :param name: model's name.
        :type name: str.
        """
        self.model.save_weights(self.name)

    def predict(self, input):
        return self.model.predict(input)

