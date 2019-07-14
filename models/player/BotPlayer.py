from models.player.Player import Player
from learning.ImitationNetwork import NeuralNetwork


class BotPlayer(Player):
    def __init__(self, scene, x, y, number, initial_lives=Player.INITIAL_LIVES, score=0):
        super().__init__(scene, x, y, number, initial_lives, score)

        # This bot runs a classifying neural network to predict which actions it should take
        # Inputs:
        #   x and y of player (normalized)
        #   x and y of player's speed
        #   direction of player
        #   x and y of closest enemy (normalized) in each of 4 circular sections
        #   x and y of closest enemy's speed
        #
        # Outputs:
        #   forward
        #   turn right
        #   turn left
        #   shoot
        self.neural_network = NeuralNetwork(10, 20, 4)

    def update(self, event=None, other_sprites=None):
        # self.action = self.nn.predict([self.x/self.screen.get_width(),
        #                          self.y/self.screen.get_height(),
        #                          self.direction,
        #                          ])

        super().update(event, other_sprites)

    def check_self_collision(self, sprites_group):
        pass
