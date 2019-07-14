import csv
import numpy as np
from keras import models, layers, losses, optimizers, activations, metrics, regularizers
from utils.constants import N_INPUTS, N_OUTPUTS

FORWARD_MODEL = 0
SHOOT_MODEL = 1
TURN_MODEL = 2


class ImitationNetwork:
    N_INPUTS = N_INPUTS
    N_HIDDEN = 50
    N_OUTPUTS = N_OUTPUTS

    def __init__(self, name):
        self.name = 'imitation_network'

        self.model = models.Sequential()
        alpha = 0.01  # LeakyRelu alpha
        lambda_l2 = 0.3  # lambda parameter of the L2 regularization

        self.model.add(layers.Dense(self.N_INPUTS, input_shape=(17,), activation=activations.linear))
        self.model.add(layers.LeakyReLU(alpha))
        self.model.add(layers.Dense(self.N_HIDDEN, input_shape=(17,), activation=activations.linear))
        self.model.add(layers.LeakyReLU(alpha))
        self.model.add(layers.Dense(self.N_HIDDEN, activation=activations.sigmoid,
                       kernel_regularizer=regularizers.l2(lambda_l2)))
        self.model.add(layers.Dense(self.N_OUTPUTS, activation=activations.sigmoid,
                       kernel_regularizer=regularizers.l2(lambda_l2)))

        self.model.compile(optimizer=optimizers.Adam(), loss=losses.binary_crossentropy,
                           metrics=[metrics.binary_accuracy])

    def fit(self, file_name):
        num_epochs = 5000  # number of epochs for training
        input_file = open(file_name, 'r')
        rows = csv.reader(input_file)
        inputs = []
        outputs = []
        for row in rows:
            inputs.append(row[1:18])
            outputs.append(row[18:22])

        inputs = np.matrix(inputs)
        outputs = np.matrix(outputs)
        self.model.fit(inputs, outputs, batch_size=inputs.shape[0]//4, epochs=num_epochs)
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

