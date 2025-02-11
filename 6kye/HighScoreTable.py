
# Now all you need is a high score table that can be updated with the player's final scores.
# With such a feature, the player will be motivated to try to beat his previous scores,
# and hopefully, never stop playing your game.

# The high score table will start out empty.
# A limit to the size of the table will be specified upon creation of the table.

class HighScoreTable:

    def __init__(self, limit):
        self.limit = limit
        self.scores = []

    def update(self, score):
        self.scores.append(score)
        self.scores.sort(reverse=True)
        self.scores = self.scores[:self.limit]

    def reset(self):
        self.scores = []
