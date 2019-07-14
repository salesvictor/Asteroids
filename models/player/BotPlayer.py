from models.player.Player import Player
from utils.constants import FORWARD, TURN_LEFT, TURN_RIGHT, SHOOT
from learning.SupervisedNetwork import ImitationNetwork, FORWARD_MODEL, SHOOT_MODEL, TURN_MODEL
import numpy as np


class BotPlayer(Player):
    def __init__(self, scene, x, y, neural_network, number=1, initial_lives=Player.INITIAL_LIVES, score=0):
        super().__init__(scene, x, y, number, initial_lives, score)

        self.network = neural_network(self.name)
        self.network.load()

    def update(self, event=None, other_sprites=None):
        super().update(event, other_sprites)

        predicts = self.network.predict(self.input)
        print (predicts)
        if predicts[0, FORWARD] >= 0.5:
            self.action[FORWARD] = True
            self.forward()
        if predicts[0, TURN_LEFT] > predicts[0, TURN_RIGHT] and predicts[0, TURN_LEFT] >= 0.5:
            self.action[TURN_LEFT] = True
            self.turn(-self.TURN_SPEED)
        if predicts[0, TURN_RIGHT] > predicts[0, TURN_LEFT] and predicts[0, TURN_RIGHT] >= 0.5:
            self.action[TURN_RIGHT] = True
            self.turn(self.TURN_SPEED)
        if predicts[0, SHOOT] >= 0.5:
            self.action[SHOOT] = True
            self.shoot()
