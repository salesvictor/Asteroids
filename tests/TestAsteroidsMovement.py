import pygame
from models.SmallAsteroid import SmallAsteroid
from models.MediumAsteroid import MediumAsteroid
from models.BigAsteroid import BigAsteroid

if __name__ == '__main__':
    FPS = 60
    SCREEN_W = 800
    SCREEN_H = 600
    SIZE = (SCREEN_W, SCREEN_H)

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Asteroid Testing')

    asteroids = pygame.sprite.Group()
    for i in range(12):
        if i % 3 == 0:
            asteroids.add(SmallAsteroid(screen))
        elif i % 3 == 1:
            asteroids.add(MediumAsteroid(screen))
        else:
            asteroids.add(BigAsteroid(screen))

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                break

        screen.fill((0, 0, 0))

        asteroids.update()
        asteroids.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
