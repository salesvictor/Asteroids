import pygame
from math import cos, sin, radians
from models.Ship import Ship

if __name__ == '__main__':
    FPS = 60
    SCREEN_W = 800
    SCREEN_H = 600
    SIZE = (SCREEN_W, SCREEN_H)

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
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

        print(f'(pos, center, direction, speed, vel_dir) = '
              f'(({player.x, player.y}), {player.rect.center}, '
              f'{player.direction}, {player.speed:.2f}, '
              f'({player.vel_dir[0]:.2f}, {player.vel_dir[1]:.2f}))')

        screen.fill((0, 0, 0))

        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
