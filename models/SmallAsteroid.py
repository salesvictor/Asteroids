from models.Asteroid import Asteroid


class SmallAsteroid(Asteroid):

    def __init__(self, screen, x=None, y=None, speed=None, vel_dir=None):
        super().__init__(screen, 'small_asteroid.png', 1.0, x, y, speed, vel_dir)