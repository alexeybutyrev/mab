import random
from .mab import MAB
from random import choices
from math import exp


class Softmax(MAB):
    def __init__(self, temperature=0.1, counts=None, values=None, n_arms=None):
        super().__init__(counts, values, n_arms)
        self.temperature = temperature  # parameter of the algorythm

    @property
    def name(self):
        return "Softmax. T=" + str(self.temperature)

    def select_arm(self):
        # update epsilon if weaknes multipler was set
        probs = [exp(v/self.temperature) for v in self.values]
        scale_denomiator = sum(probs)
        probs = [p / scale_denomiator for p in probs]

        return choices(range(self.n_arms), weights=probs)[0]
