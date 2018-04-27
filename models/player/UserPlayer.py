import pygame as pg

from models.player.Player import Player


class UserPlayer(Player):
    def __init__(self, screen, x, y, number, initial_lives=Player.INITIAL_LIVES,
                 score=0):
        super().__init__(screen, x, y, number, initial_lives, score)

    # Update based on keyboard events
    def update(self, event=None, other_sprites=None):
        # if event.type == pg.KEYDOWN:
        #   if event.key == pg.K_SPACE:
        #        self.shoot()

        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.forward()
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.turn(-self.TURN_SPEED)
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.turn(self.TURN_SPEED)
        if keys[pg.K_SPACE]:
            self.shoot()

        super().update(event, other_sprites)
