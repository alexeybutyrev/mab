import random
from .mab import MAB


class RandomSelect(MAB):
    def __init__(self, counts=None, values=None, n_arms=None):
        super().__init__(counts, values, n_arms)

    @property
    def name(self):
        return "RandomSelect"

    def select_arm(self):
        return random.randint(0, self.n_arms-1)
