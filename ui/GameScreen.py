import pygame as pg

from ui.ScreenBase import ScreenBase
from ui.GameOverScreen import GameOverScreen
from player.UserPlayer import UserPlayer
from models.SmallAsteroid import SmallAsteroid
from models.MediumAsteroid import MediumAsteroid
from models.BigAsteroid import BigAsteroid


class GameScreen(ScreenBase):
    def __init__(self, display):
        super().__init__(display)

        # Create players
        self.player = UserPlayer(display, display.get_width()/2, display.get_height()/2, 1)
        self.players = [self.player]
        self.visible_players = pg.sprite.Group()
        self.visible_players.add(self.player)

        # Create background asteroids
        self.asteroids = pg.sprite.Group()
        for i in range(12):
            if i % 3 == 0:
                self.asteroids.add(SmallAsteroid(display))
            elif i % 3 == 1:
                self.asteroids.add(MediumAsteroid(display))
            else:
                self.asteroids.add(BigAsteroid(display))

    def update(self, event):
        # Make all collisions
        for player in self.visible_players:
            player.check_bullets_collision(self.asteroids)

        pg.sprite.groupcollide(self.visible_players, self.asteroids, True, True, pg.sprite.collide_mask)

        # Look for non-permanently-dead players (which aren't within any group of sprites)
        # and initialize new players to them
        for player in self.players:
            if player not in self.visible_players and player.lives > 0:
                reset_player = UserPlayer(player.screen, player.initialx, player.initialy, player.number, player.lives)
                self.players.remove(player)
                self.players.append(reset_player)
                self.visible_players.add(reset_player)

        # Update objects movement
        self.visible_players.update(event)
        self.asteroids.update()

        # Check if all players have permanently died and, if so, ends the game
        game_over = True
        for player in self.players:
            if player.lives > 0:
                game_over = False
                break

        if game_over:
            self.switch_to_scene(GameOverScreen(self.display, self.players, self.asteroids))

    # Render all text boxes and draw all sprites
    def render(self):
        self.display.fill(self.BG_COLOR)
        for player in self.players:
            player.render()
        self.visible_players.draw(self.display)
        for player in self.visible_players:
            player.shot_bullets.draw(self.display)
        self.asteroids.draw(self.display)
