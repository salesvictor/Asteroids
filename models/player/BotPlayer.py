from models.player.Player import Player
from neural_network.NeuralNetwork import NeuralNetwork
from math import cos, sin, atan2, pi, sqrt, radians
import numpy as np
import pygame as pg


class BotPlayer(Player):
    SIGHT_RADIUS = 500

    def __init__(self, scene, x, y, number, initial_lives=Player.INITIAL_LIVES, score=0):
        super().__init__(scene.display, x, y, number, initial_lives, score)

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
        self.nn = NeuralNetwork(10, 20, 4)
        self.closest_enemy = [None] * 4
        self.scene = scene

    def update(self, event=None, other_sprites=None):
        # rotation to be aplied for a system with origin rotated by pi/4 relatively to the ship
        c, s = cos(radians(self.direction) - pi/4), sin(radians(self.direction) - pi/4)
        rot = np.asmatrix([[c, s], [-s, c]])

        self.closest_enemy = [None] * 4

        for sprite in self.scene.active_sprites:
            if sprite.__class__.__name__ in ['Asteroid', 'BigAsteroid', 'MediumAsteroid', 'SmallAsteroid',
                                             'Saucer', 'BigSaucer', 'SmallSaucer']:
                # move the toroidal space center to ship position
                enemy_pose = np.asmatrix([sprite.x - self.x, sprite.y - self.y])
                (width, height) = self.screen.get_size()

                if enemy_pose[0, 0] < -width/2:
                    enemy_pose[0, 0] += width
                elif enemy_pose[0, 0] > width/2:
                    enemy_pose[0, 0] -= width

                if enemy_pose[0, 1] < -height/2:
                    enemy_pose[0, 1] += height
                elif enemy_pose[0, 1] > height/2:
                    enemy_pose[0, 1] -= height

                # applying rotation over enemy relative position
                enemy_pose *= rot

                # checking in which area of sight the asteroid is located
                distance = sqrt(enemy_pose[0, 0] ** 2 + enemy_pose[0, 1] ** 2)
                if distance < self.SIGHT_RADIUS:
                    angle = pi + atan2(enemy_pose[0, 0], enemy_pose[0, 1])
                    if 0 < angle <= pi/2:
                        index = 0
                    elif pi/2 < angle <= pi:
                        index = 1
                    elif pi < angle <= 3*pi/2:
                        index = 2
                    else:
                        index = 3

                    if not self.closest_enemy[index] or self.closest_enemy[index][1] > distance:
                        self.closest_enemy[index] = (sprite, distance)

        # action = self.nn.predict([self.x/self.screen.get_width(),
        #                          self.y/self.screen.get_height(),
        #                          self.direction,
        #                          ])

    def check_self_collision(self, sprites_group):
        pass

    def draw_debug(self):
        start_pos = (self.x, self.y)
        end_pos = (start_pos[0] + 100*cos(radians(self.direction)), start_pos[1] + 100*sin(radians(self.direction)))
        pg.draw.line(self.scene.display, (255, 255, 255), start_pos, end_pos)
        for i in range(4):
            angle = radians(self.direction) - pi/4 + i*pi/2
            end_pos = (start_pos[0] + self.SIGHT_RADIUS*cos(angle), start_pos[1] + self.SIGHT_RADIUS*sin(angle))
            pg.draw.line(self.scene.display, (255, 255, 255), start_pos, end_pos)
            if self.closest_enemy[i]:
                self.scene.display.blit(self.closest_enemy[i][0].mask_surface, self.closest_enemy[i][0].rect)
