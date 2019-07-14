import pygame as pg

from models.Ship import Ship
from ui.text.TextBox import TextBox
from ui.text.LivesBar import LivesBar
from score.ScoreCounter import ScoreCounter
from math import sin, cos, pi, radians, sqrt, atan2
import numpy as np
import csv
import os

# Actions
FORWARD = 0
TURN_LEFT = 1
TURN_RIGHT = 2
SHOOT = 3


class Player(Ship):
    # General constants
    INITIAL_LIVES = 3
    MAX_LIVES = 5
    NAME_BOX_FONT_SIZE = 20
    SCORE_BOX_FONT_SIZE = 20
    RESPAWN_TIME = 20
    SPAWN_AREA_COLLIDE_RATIO = 1.2
    SIGHT_RADIUS = 500

    def __init__(self, scene, x, y, number, initial_lives=INITIAL_LIVES,
                 score=0):
        super().__init__(scene.display, x, y)
        self.initialx = x
        self.initialy = y

        self.lives = min(initial_lives, self.MAX_LIVES)
        self.score = score
        self.number = number
        self.name = f"PLAYER{number}"
        self.screen = scene.display

        # Dead state
        self.is_visible = True
        self.time_to_respawn = 0
        self.spawn_area_collide = pg.sprite.collide_circle_ratio(self.SPAWN_AREA_COLLIDE_RATIO)

        # Create an score counter for the player
        self.score_counter = ScoreCounter()

        # Calculate position of text boxes and lives bar
        self.display_width_factor = scene.display.get_width() / 800
        self.display_height_factor = scene.display.get_height() / 640
        self.NAME_BOX_CENTER = (self.display_width_factor * 100,
                                self.display_height_factor * 25)
        self.SCORE_BOX_CENTER = (self.NAME_BOX_CENTER[0],
                                 self.NAME_BOX_CENTER[1] + 25)
        self.LIVES_BAR_CENTER = (self.SCORE_BOX_CENTER[0],
                                 self.SCORE_BOX_CENTER[1] + 30)

        # Create text boxes and lives bar
        self.name_box = TextBox(self.screen, self.NAME_BOX_CENTER,
                                self.NAME_BOX_FONT_SIZE, self.name)
        self.score_box = TextBox(self.screen, self.SCORE_BOX_CENTER,
                                 self.SCORE_BOX_FONT_SIZE, f"{self.score}")
        self.lives_bar = LivesBar(self.LIVES_BAR_CENTER, self.lives)

        # Modeling attributes
        self.closest_enemy = [None] * 4
        self.scene = scene

        # Actions mapping
        self.action = [False] * 4

        # Logging
        self.log_file_name = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "db/player_log.csv")
        self.log_file = None

    def add_life(self):
        self.lives = min(self.MAX_LIVES, self.lives+1)
        self.lives_bar.set_lives(self.lives)

    def add_score(self, points):
        self.score += points

        # For each 10,000 points, add an extra life:
        if self.score//10000 > (self.score - points)//10000:
            self.add_life()

    # Check for collisions of the players bullets with other objects
    def check_bullets_collision(self, sprites_group):
        collisions = super().check_bullets_collision(sprites_group)
        for collision in collisions:
            event = collision.__class__.__name__
            self.score_counter.add_score(self, event)

    # Check for collisions off the player with other objects
    def check_self_collision(self, sprites_group):
        collisions = super().check_self_collision(sprites_group)
        for collision in collisions:
            event = collision.__class__.__name__
            self.score_counter.add_score(self, event)

    # Respawn the player at the initial (x,y) position
    def respawn(self, other_sprites=None):
        super().__init__(self.screen, self.initialx, self.initialy)
        safe_spawn = True
        if other_sprites is not None:
            for sprite in other_sprites:
                if self.spawn_area_collide(self, sprite):
                    safe_spawn = False

        if safe_spawn:
            self.is_visible = True

    # Update the object based on input events
    def update(self, event=None, other_sprites=None):
        self.model()

        if not self.is_visible and self.lives > 0:
            if self.time_to_respawn > 0:
                self.time_to_respawn -= 1
            elif self.time_to_respawn == 0:
                self.respawn(other_sprites)

        else:
            # Change the score displayed
            self.score_box.set_dialogue(f"{self.score}")
            super().update()

    # Render the text boxes and lives bar
    def render(self):
        self.name_box.render()
        self.score_box.render()
        self.lives_bar.render(self.screen)

    # Remove the player from all its groups without reducing its lives
    def vanish(self):
        super().kill()
        self.is_visible = False

    # Eliminate the player from the current groups
    def kill(self):
        super().kill()
        self.lives -= 1
        self.lives_bar.set_lives(self.lives)

        self.is_visible = False

        if self.lives != 0:
            self.time_to_respawn = self.RESPAWN_TIME

    # Model world inputs to the player
    def model(self):
        # rotation to be aplied for a system with origin rotated by pi/4 relatively to the ship
        c, s = cos(radians(self.direction) - pi / 4), sin(radians(self.direction) - pi / 4)
        rot = np.asmatrix([[c, s], [-s, c]])

        self.closest_enemy = [None] * 4

        for sprite in self.scene.active_sprites:
            if sprite.__class__.__name__ in ['Asteroid', 'BigAsteroid', 'MediumAsteroid', 'SmallAsteroid',
                                             'Saucer', 'BigSaucer', 'SmallSaucer']:
                # move the toroidal space center to ship position
                enemy_pose = np.asmatrix([sprite.x - self.x, sprite.y - self.y])
                (width, height) = self.screen.get_size()

                if enemy_pose[0, 0] < -width / 2:
                    enemy_pose[0, 0] += width
                elif enemy_pose[0, 0] > width / 2:
                    enemy_pose[0, 0] -= width

                if enemy_pose[0, 1] < -height / 2:
                    enemy_pose[0, 1] += height
                elif enemy_pose[0, 1] > height / 2:
                    enemy_pose[0, 1] -= height

                # applying rotation over enemy relative position
                enemy_pose *= rot

                # checking in which area of sight the asteroid is located
                distance = sqrt(enemy_pose[0, 0] ** 2 + enemy_pose[0, 1] ** 2)
                if distance < self.SIGHT_RADIUS:
                    angle = pi + atan2(enemy_pose[0, 0], enemy_pose[0, 1])
                    if 0 < angle <= pi / 2:
                        index = 0
                    elif pi / 2 < angle <= pi:
                        index = 1
                    elif pi < angle <= 3 * pi / 2:
                        index = 2
                    else:
                        index = 3

                    if not self.closest_enemy[index] or self.closest_enemy[index][1] > distance:
                        self.closest_enemy[index] = (sprite, distance)

    # Function to log players modeling and actions
    def log(self):
        if not self.log_file:
            if os.path.exists(self.log_file_name):
                self.log_file = open(self.log_file_name, 'a+')
            else:
                self.log_file = open(self.log_file_name, 'w+')

        log_writer = csv.writer(self.log_file)

        data = [self.name,
                self.x,
                self.y,
                self.speed[0],
                self.speed[1],
                self.direction]

        for enemy in self.closest_enemy:
            if enemy:
                data.extend([True, enemy[0].x, enemy[0].y, enemy[0].speed[0], enemy[0].speed[1]])
            else:
                data.extend([False, 0.0, 0.0, 0.0, 0.0])

        data.extend(self.action)
        data.append(self.score)

        log_writer.writerow(data)

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
