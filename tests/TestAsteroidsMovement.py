import pygame as pg
from models.SmallAsteroid import SmallAsteroid
from models.MediumAsteroid import MediumAsteroid
from models.BigAsteroid import BigAsteroid

def change_color(screen):
    color = screen.get_at((0, 0))

    if color == (0, 0, 0):
        return (0, 0, 255)
    else:
        return (0, 0, 0)


if __name__ == '__main__':
    FPS = 60
    SCREEN_W = 800
    SCREEN_H = 600
    SIZE = (SCREEN_W, SCREEN_H)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)

    bg_color = BLACK

    pg.init()

    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption('Asteroid Movement Testing')
    clock = pg.time.Clock()

    asteroids = pg.sprite.Group()
    for i in range(12):
        if i % 3 == 0:
            asteroids.add(SmallAsteroid(screen))
        elif i % 3 == 1:
            asteroids.add(MediumAsteroid(screen))
        else:
            asteroids.add(BigAsteroid(screen))

    while True:
        ev = pg.event.poll()
        if ev.type == pg.QUIT:
            break
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                break
            if ev.key == pg.K_SPACE:
                bg_color = change_color(screen)

        screen.fill(bg_color)

        asteroids.update()
        asteroids.draw(screen)

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()
