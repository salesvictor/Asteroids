from models.player.Player import Player
from neural_network.NeuralNetwork import NeuralNetwork


class BotPlayer(Player):
    def __init__(self, screen, x, y, number, initial_lives=1, score=0):
        super().__init__(screen, x, y, number, initial_lives, score)

        # Inputs:
        #   x and y of player (normalized)
        #   x and y of player's speed
        #   direction of player
        #   x and y of nearest enemy (normalized)
        #   x and y of nearest enemy's speed
        #   distance to nearest enemy
        #
        # Outputs:
        #   forward
        #   turn right
        #   turn left
        #   shoot
        self.nn = NeuralNetwork(10, 20, 4)

    def update(self, event=None, other_sprites=None):
        nearest_enemy = None
        max_dist = self.screen.get_width()**2 + self.screen.get_height()**2
        min_dist =
        for sprite in self.screen.active_sprites:
            if sprite.__class__.__name__ in ['Asteroid', 'BigAsteroid', 'MediumAsteroid', 'SmallAsteroid',
                                             'Saucer', 'BigSaucer', 'SmallSaucer']
                and (self.x-sprite.x)**2 + (self.y-sprite.y)**2:



        action = self.nn.predict([self.x/self.screen.get_width(),
                                  self.y/self.screen.get_height(),
                                  self.direction,
                                  ])