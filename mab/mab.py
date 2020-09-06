import random


class MAB():
    """
    Mulitarm Bandint base class
    """

    def __init__(self, counts=None, values=None, n_arms=None):
        if counts is None:
            # set up with zeroes if not defined
            assert n_arms is not None
            counts = [0] * n_arms
            values = [0.0] * n_arms

        self.n_arms = len(counts)
        self.counts = counts  # number of counts chose for each arm
        self.values = values  # success rate for each arm

    def __str__(self):
        return str(self.__class__.__name__)

    def reset(self):
        self.counts = [0] * self.n_arms
        self.values = [0.0] * self.n_arms

    def select_arm(self):
        # Define here when inheriting
        pass

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        self.values[chosen_arm] = ((n-1) / n) * self.values[chosen_arm] + reward / n
