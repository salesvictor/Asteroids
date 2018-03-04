import pygame as pg
from models.Ship import Ship

if __name__ == '__main__':
    FPS = 60
    SCREEN_W = 800
    SCREEN_H = 600
    SIZE = (SCREEN_W, SCREEN_H)
    BLACK = (0, 0, 0)

    pg.init()

    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption('Ship Shooting Test')
    clock = pg.time.Clock()

    # Creates a sprite list for drawing
    sprites = pg.sprite.Group()

    # Creates a new ship and adds it to the sprite list
    player = Ship(screen, SCREEN_W//2, SCREEN_H//2)
    sprites.add(player)

    while True:
        ev = pg.event.poll()
        if ev.type == pg.QUIT:
            break
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                break
        if ev.type == pg.KEYUP:
            if ev.key == pg.K_SPACE:
                player.shoot()
                sprites.add(player.shot_bullets[-1])

        screen.fill(BLACK)

        sprites.update()
        sprites.draw(screen)
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()
