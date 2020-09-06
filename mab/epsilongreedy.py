import random
from .mab import MAB


class EpsilonGreedy(MAB):
    def __init__(self, epsilon=1.0, counts=None, values=None, n_arms=None, weakness_mult=None):
        super().__init__(counts, values, n_arms)
        self.epsilon = epsilon  # probablity of choosing random arm
        self.weakness_mult = None
        if weakness_mult is not None:
            self.weakness_mult = weakness_mult
            self.epsilon = 1.0

    @property
    def name(self):
        if self.weakness_mult is None:
            return "EpsilonGreedy - " + str(self.epsilon)
        else:
            return "EpsilonWeakGreedy - " + str(self.weakness_mult)

    def select_arm(self):
        # update epsilon if weaknes multipler was set
        if self.weakness_mult is not None:
            self.epsilon *= self.weakness_mult

        def argmax(x): return max(enumerate(x), key=lambda x: x[1])[0]

        if random.random() > self.epsilon:
            return argmax(self.values)
        else:
            return random.randint(0, self.n_arms-1)
