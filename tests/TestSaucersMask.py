import pygame as pg
from models.SmallSaucer import SmallSaucer
from models.BigSaucer import BigSaucer
from models.player.UserPlayer import UserPlayer

if __name__ == '__main__':
    FPS = 60
    SCREEN_W = 800
    SCREEN_H = 600
    SIZE = (SCREEN_W, SCREEN_H)
    BLACK = (0, 0, 0)

    pg.init()
    pg.font.init()

    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption('Saucer Test')
    my_font = pg.font.SysFont('Times New Roman', 20)
    clock = pg.time.Clock()

    # Creates a sprite list for drawing
    saucers = pg.sprite.Group()

    # Create players
    player = UserPlayer(screen, screen.get_width()//2,
                             screen.get_height()//2, 1)
    players = [player]
    visible_players = pg.sprite.Group()
    visible_players.add(player)

    # Creates 2 saucers
    big_saucer = BigSaucer(screen)
    small_saucer = SmallSaucer(screen, player)

    saucers.add(big_saucer)
    saucers.add(small_saucer)

    while True:
        ev = pg.event.poll()
        if ev.type == pg.QUIT:
            break
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                break
            if ev.key == pg.K_SPACE:
                for saucer in saucers:
                    saucer.kill()

        debug_text = f"bullet timer: {big_saucer.bullet_timer}"
        text_surface = my_font.render(debug_text, True, (255, 255, 255))
        (font_w, font_h) = text_surface.get_size()

        screen.fill(BLACK)

        saucers.update()
        player.update(ev)
        for player in players:
            player.render()
        visible_players.draw(screen)
        for player in visible_players:
            player.shot_bullets.draw(screen)
        saucers.draw(screen)
        for saucer in saucers:
            saucer.saucer_shot_bullets.draw(screen)
        screen.blit(text_surface, ((SCREEN_W-font_w)/2, 0))

        # Get the outline of the mask then draw its points in the screen
        for saucer in saucers:
            olist = saucer.mask.outline()
            true_olist = []
            for point in olist:
                true_point = (point[0] + saucer.rect.topleft[0], point[1] + saucer.rect.topleft[1])
                true_olist.append(true_point)

            if len(true_olist) > 2:
                pg.draw.polygon(screen, (200, 150, 150), true_olist, 0)

        pg.display.flip()

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()
