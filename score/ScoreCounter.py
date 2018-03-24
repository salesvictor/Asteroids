class ScoreCounter(object):
    # Assignment of the points given for each event
    BIG_ASTEROID_SCORE = 20
    MEDIUM_ASTEROID_SCORE = 50
    SMALL_ASTEROID_SCORE = 100
    BIG_SAUCER_SCORE = 200
    SMALL_SAUCER_SCORE = 1000

    # Method that changes the score off a player based on the event passed
    def add_score(self, player, event):
        if event == 'BigAsteroid':
            player.add_score(self.BIG_ASTEROID_SCORE)
        elif event == 'MediumAsteroid':
            player.add_score(self.MEDIUM_ASTEROID_SCORE)
        elif event == 'SmallAsteroid':
            player.add_score(self.SMALL_ASTEROID_SCORE)
        elif event == 'BigSaucer':
            player.add_score(self.BIG_SAUCER_SCORE)
        elif event == 'SmallSaucer':
            player.add_score(self.SMALL_SAUCER_SCORE)
