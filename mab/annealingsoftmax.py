import random
from .softmax import Softmax
from math import log


class AnnealingSoftmax(Softmax):
    def __init__(self, counts=None, values=None, n_arms=None):
        super().__init__(1.0, counts, values, n_arms)

    @property
    def name(self):
        return "AnnealingSoftmax"

    def select_arm(self):
        t = sum(self.counts) + 1
        self.temperature = 1.0/log(t + 0.0000001)
        # update epsilon if weaknes multipler was set
        return super(AnnealingSoftmax, self).select_arm()
