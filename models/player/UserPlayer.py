import pygame as pg

from models.player.Player import Player
from utils.constants import FORWARD, TURN_LEFT, TURN_RIGHT, SHOOT


class UserPlayer(Player):
    def __init__(self, scene, x, y, number, initial_lives=Player.INITIAL_LIVES,
                 score=0):
        super().__init__(scene, x, y, number, initial_lives, score)

    # Update based on keyboard events
    def update(self, event=None, other_sprites=None):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.action[FORWARD] = True
            self.forward()
        else:
            self.action[FORWARD] = False

        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.action[TURN_LEFT] = True
            self.turn(-self.TURN_SPEED)
        else:
            self.action[TURN_LEFT] = False

        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.action[TURN_RIGHT] = True
            self.turn(self.TURN_SPEED)
        else:
            self.action[TURN_RIGHT] = False

        if keys[pg.K_SPACE]:
            self.action[SHOOT] = True
            self.shoot()
        else:
            self.action[SHOOT] = False

        super().update(event, other_sprites)
