import pygame
from math import cos, sin, radians
from models.Ship import Ship

if __name__ == '__main__':
    FPS = 60
    SCREEN_W = 640
    SCREEN_H = 480

    size = (SCREEN_W, SCREEN_H)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Ship Testing')

    # Creates a sprite list for drawing
    sprites = pygame.sprite.Group()

    # Creates a new ship and adds it to the sprite list
    player = Ship(screen, SCREEN_W//2, SCREEN_H//2)
    sprites.add(player)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player.accelerate((cos(radians(player.direction)), sin(radians(player.direction))))
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.turn(5)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.turn(-5)
        if not keys[pygame.K_w] and not keys[pygame.K_UP]:
            player.stop()

        screen.fill((0, 0, 0))

        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
