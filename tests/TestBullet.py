import pygame
from math import atan, degrees, pi
from models.Bullet import Bullet

if __name__ == '__main__':
    FPS = 60
    SCREEN_W = 800
    SCREEN_H = 600

    size = (SCREEN_W, SCREEN_H)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Bullets Testing')

    # Creates a sprite list for drawing
    sprites = pygame.sprite.Group()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            # Creates a new bullet to go through the clicked direction and adds it to the sprite list
            click_pos = ev.dict["pos"]
            direction = atan((click_pos[1]-SCREEN_H/2) / (click_pos[0]-SCREEN_W/2))
            if click_pos[0] < SCREEN_W/2:
                direction += pi

            direction = degrees(direction)

            print(direction)

            bullet = Bullet(screen, SCREEN_W/2, SCREEN_H/2, direction)
            sprites.add(bullet)

        screen.fill((0, 0, 0))

        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
