import pygame as pg
import os
import sys

from random import randint

from ui.screen.ScreenBase import ScreenBase
from score.ScoreCounter import ScoreCounter
from models.player.BotPlayer import BotPlayer
from models.asteroid.SmallAsteroid import SmallAsteroid
from models.asteroid.MediumAsteroid import MediumAsteroid
from models.asteroid.BigAsteroid import BigAsteroid
from models.saucer.BigSaucer import BigSaucer
from models.saucer.SmallSaucer import SmallSaucer
from assets.sfx.Sounds import Sounds


class TrainerScreen(ScreenBase):
    def __init__(self, display):
        super().__init__(display)

        # Setting sounds
        self.sounds = Sounds()
        Sounds.stop_title_song()

        # Factor for decreasing of the beat period
        self.period_factor = 3e-4

        # Create a score counter to assign each player's score
        self.score_counter = ScoreCounter()

        # Create players
        self.player = BotPlayer(self, display.get_width()//2,
                                 display.get_height()//2, 1, 1)
        self.players = [self.player]
        self.visible_players = pg.sprite.Group()
        self.visible_players.add(self.player)

        # Round counter
        self.round = 1

        # Flag for game over
        self.game_over = False

        # Create background asteroids
        self.asteroids = pg.sprite.Group()
        for i in range(12):
            if i % 3 == 0:
                self.asteroids.add(SmallAsteroid(display))
            elif i % 3 == 1:
                self.asteroids.add(MediumAsteroid(display))
            else:
                self.asteroids.add(BigAsteroid(display))

        # Create a variable for counting time since last saucer died
        self.frames_since_saucer = 0
        self.SAUCER_SPAWN_TIME = 2000
        self.saucers = pg.sprite.Group()

        # Add all sprites to active sprites group
        self.active_sprites.add(self.visible_players)
        for player in self.visible_players:
            self.active_sprites.add(player.shot_bullets)
        self.active_sprites.add(self.saucers)
        for saucer in self.saucers:
            self.active_sprites.add(saucer.saucer_shot_bullets)
        self.active_sprites.add(self.asteroids)

    def update(self, event):
        super().update(event)

        # Play back beat
        self.sounds.theme_song()
        self.sounds.set_period(self.sounds.period - self.period_factor)

        # If esc is pressed, switch to settings screen
        # if event.type == pg.KEYDOWN:
        #    if event.key == pg.K_ESCAPE:
        #       self.switch_to_scene(SettingsScreen(self.display, self, self.active_sprites))

        # Todo: Create a random saucer class to instantiate a random saucer, and maybe variate this based on round
        # Create a random saucer
        if not self.saucers.__nonzero__():
            self.frames_since_saucer += 1

        if self.frames_since_saucer >= self.SAUCER_SPAWN_TIME:
            i = randint(1, 2)
            if i == 1:
                saucer = BigSaucer(self.display)
            else:
                saucer = SmallSaucer(self.display, self.round, self.player)

            self.saucers.add(saucer)
            self.active_sprites.add(self.saucers)
            for saucer in self.saucers:
                self.active_sprites.add(saucer.saucer_shot_bullets)

            # Whenever the first saucer appears in a round, other saucers will spawn
            # more often until the round is over
            self.frames_since_saucer = 1200 + randint(1, 5) * 100

        # Todo: Create a round function to call rounds
        # If game is not over and all asteroids and saucers were destroyed, call a new round
        if not (self.asteroids.__nonzero__() or self.saucers.__nonzero__()):
            self.round += 1

            # Reset back beat period
            self.sounds.set_period(Sounds.INITIAL_PERIOD)

            # Create asteroids
            for i in range(12):
                if i % 3 == 0:
                    self.asteroids.add(SmallAsteroid(self.display))
                elif i % 3 == 1:
                    self.asteroids.add(MediumAsteroid(self.display))
                else:
                    self.asteroids.add(BigAsteroid(self.display))

            # Add all sprites to active sprites group
            self.active_sprites.add(self.visible_players)
            for player in self.visible_players:
                self.active_sprites.add(player.shot_bullets)
            self.active_sprites.add(self.asteroids)

            # Respawn all visible players in their initial positions
            for player in self.visible_players:
                player.vanish()
                player.respawn()

            # Restart saucers time counting
            self.frames_since_saucer = 0

        # Make all collisions
        for player in self.players:
            player.check_bullets_collision(self.asteroids)
            player.check_bullets_collision(self.saucers)
        for player in self.visible_players:
            player.check_self_collision(self.asteroids)
            player.check_self_collision(self.saucers)
            for saucer in self.saucers:
                player.check_self_collision(saucer.saucer_shot_bullets)

        # Look for respawned players and add them again to visible players
        for player in self.players:
            if player not in self.visible_players and player.is_visible:
                self.visible_players.add(player)
                self.active_sprites.add(player)

        # Update all active sprites but the players
        for sprite in self.active_sprites:
            if sprite.__class__.__name__ not in ['Player', 'UserPlayer', 'BotPlayer']:
                sprite.update()
        for saucer in self.saucers:
            self.active_sprites.add(saucer.saucer_shot_bullets)

        # Update players based on active sprites
        for player in self.players:
            player.update(event, self.active_sprites)
            self.active_sprites.add(player.shot_bullets)

        # Check if all players have permanently died and, if so, ends the game
        # self.game_over = True
        # for player in self.players:
        #    if player.lives > 0:
        #        self.game_over = False
        #        break

        # if self.game_over:
        #    self.switch_to_scene(GameOverScreen(self.display, self.players,
        #                                        self.active_sprites))

    # Render all text boxes and draw all sprites
    def render(self):
        self.display.fill(self.BG_COLOR)
        for player in self.players:
            player.render()
            player.draw_debug()
        self.active_sprites.draw(self.display)


def main(args, fps):
    if not args:
        size = (640, 480)
    elif len(args) == 2:
        size = (float(args[1]), float(args[2]))
    else:
        print('Usage:\n  asteroids.py width heigth.\nExample:\n  asteroids.py 800 640\n')
        return

    os.makedirs('db', exist_ok=True)
    pg.mixer.pre_init(44100, -16, 2,  512)
    pg.init()
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    active_scene = TrainerScreen(screen)

    while active_scene is not None:
        # Process the filtered_events and update the frame
        event = active_scene.process_input()
        active_scene.update(event)
        active_scene.render()

        active_scene = active_scene.next

        pg.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main(sys.argv[1:], 60)
