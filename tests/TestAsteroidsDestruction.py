import pygame
from models.asteroid.BigAsteroid import BigAsteroid

if __name__ == '__main__':
    FPS = 60
    SCREEN_W = 800
    SCREEN_H = 600
    SIZE = (SCREEN_W, SCREEN_H)

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Asteroid Destruction Testing')

    asteroids = pygame.sprite.Group()
    asteroids.add(BigAsteroid(screen))

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                break
            elif ev.key == pygame.K_SPACE:
                for asteroid in asteroids:
                    asteroid.kill()

        screen.fill((0, 0, 0))

        asteroids.update()
        asteroids.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
