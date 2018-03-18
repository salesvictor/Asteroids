class ScoreCounter:
    # Enumeration of the events that can change the score
    BIG_ASTEROID = 1
    MEDIUM_ASTEROID = 2
    SMALL_ASTEROID = 3
    BIG_SAUCER = 4
    SMALL_SAUCER = 5

    # Assignment of the points given for each event
    BIG_ASTEROID_SCORE = 20
    MEDIUM_ASTEROID_SCORE = 50
    SMALL_ASTEROID_SCORE = 100
    BIG_SAUCER_SCORE = 200
    SMALL_SAUCER_SCORE = 1000

    # Method that changes the score off a player based on the event passed
    def add_score(self, player, event):
        if event == self.BIG_ASTEROID:
            player.add_score(self.BIG_ASTEROID_SCORE)
        elif event == self.MEDIUM_ASTEROID:
            player.add_score(self.MEDIUM_ASTEROID_SCORE)
        elif event == self.SMALL_ASTEROID:
            player.add_score(self.SMALL_ASTEROID_SCORE)
        elif event == self.BIG_SAUCER_SCORE:
            player.add_score(self.BIG_SAUCER_SCORE)
        elif event == self.SMALL_SAUCER_SCORE:
            player.add_score(self.SMALL_SAUCER_SCORE)
