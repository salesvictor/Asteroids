import pygame

from player.Player import Player
from math import cos, sin, radians


class UserPlayer(Player):
    def __init__(self, screen, x, y, number):
        super().__init__(screen, x, y, number)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.QUIT:
                break

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.ship.shot()
                    self.sprites.add(self.ship.shot_bullets[-1])

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.ship.accelerate((cos(radians(self.ship.direction)), sin(radians(self.ship.direction))))
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.ship.turn(5)
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.ship.turn(-5)
            if not keys[pygame.K_w] and not keys[pygame.K_UP]:
                self.ship.stop()
