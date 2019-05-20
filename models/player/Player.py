import pygame as pg

from models.Ship import Ship
from ui.text.TextBox import TextBox
from ui.text.LivesBar import LivesBar
from score.ScoreCounter import ScoreCounter
from math import sin, cos, pi


class Player(Ship):
    #  General constants
    INITIAL_LIVES = 3
    MAX_LIVES = 5
    NAME_BOX_FONT_SIZE = 20
    SCORE_BOX_FONT_SIZE = 20
    RESPAWN_TIME = 20
    SPAWN_AREA_COLLIDE_RATIO = 1.2

    def __init__(self, screen, x, y, number, initial_lives=INITIAL_LIVES,
                 score=0):
        super().__init__(screen, x, y)
        self.initialx = x
        self.initialy = y

        self.lives = min(initial_lives, self.MAX_LIVES)
        self.score = score
        self.number = number
        self.name = f"PLAYER{number}"
        self.screen = screen

        # Dead state
        self.is_visible = True
        self.time_to_respawn = 0
        self.spawn_area_collide = pg.sprite.collide_circle_ratio(self.SPAWN_AREA_COLLIDE_RATIO)

        # Create an score counter for the player
        self.score_counter = ScoreCounter()

        # Calculate position of text boxes and lives bar
        self.display_width_factor = screen.get_width() / 800
        self.display_height_factor = screen.get_height() / 640
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