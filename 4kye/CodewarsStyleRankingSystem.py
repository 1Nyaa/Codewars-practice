# Write a class called User that is used to calculate
# the amount that a user will progress through a ranking system similar to the one Codewars uses.

# Business Rules:
# $ A user starts at rank -8 and can progress all the way to 8.
# $ There is no 0 (zero) rank. The next rank after -1 is 1.
# $ Users will complete activities. These activities also have ranks.
# $ Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank
# $ The progress earned from the completed activity is relative to what the user's current rank
# is compared to the rank of the activity
# $ A user's rank progress starts off at zero,
# each time the progress reaches 100 the user's rank is upgraded to the next level
# $ Any remaining progress earned while in the previous rank will be applied towards the next rank's progress
# (we don't throw any progress away). The exception is if there is no other rank left to progress towards
# (Once you reach rank 8 there is no more progression).
# A user cannot progress beyond rank 8.
# The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8.
# Any other value should raise an error.

# The progress is scored like so:

# $ Completing an activity that is ranked the same as that of the user's will be worth 3 points
# $ Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
# $ Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored

# Completing an activity ranked higher than the current user's rank will accelerate the rank progression.
# The greater the difference between rankings the more the progression will be increased.
# The formula is 10 * d * d where d equals the difference in ranking between the activity and the user.

class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.rank_progression = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def _validate_rank(self, rank):
        if rank not in self.rank_progression:
            raise ValueError("Недопустимый ранг")

    def _rank_difference(self, activity_rank):
        return self.rank_progression.index(activity_rank) - self.rank_progression.index(self.rank)

    def inc_progress(self, activity_rank):

        self._validate_rank(activity_rank)

        if self.rank == 8:
            return

        diff = self._rank_difference(activity_rank)

        if diff == 0:
            self.progress += 3
        elif diff == -1:
            self.progress += 1
        elif diff < -1:
            return
        else:
            self.progress += 10 * diff * diff

        while self.progress >= 100:
            self.progress -= 100
            self._level_up()

    def _level_up(self):
        if self.rank < 8:
            current_rank_index = self.rank_progression.index(self.rank)
            if current_rank_index + 1 < len(self.rank_progression):
                self.rank = self.rank_progression[current_rank_index + 1]
            if self.rank == 8:
                self.progress = 0

    def get_rank(self):
        return self.rank

    def get_progress(self):
        return self.progress
