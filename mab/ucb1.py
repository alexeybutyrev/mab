import random
from .mab import MAB
from math import log, sqrt


class UCB1(MAB):
    """Upper confidence Boundary MAB Algorythm"""

    def __init__(self, counts=None, values=None, n_arms=None):
        """
        Args:
            counts ([int], optional): [description]. Defaults to None.
            values ([int], optional): [description]. Defaults to None.
            n_arms ([int], optional): [description]. Defaults to None.
        """
        super().__init__(counts, values, n_arms)

    @property
    def name(self):
        return "UCB1"

    def select_arm(self):
        # observe arms with no counts
        for arm, count in enumerate(self.counts):
            if count == 0:
                return arm

        max_ind = 0
        max_val = 0
        total_counts = sum(self.counts)

        for arm in range(self.n_arms):
            curr_value = self.values[arm] + sqrt(
                2 * log(total_counts) / float(self.counts[arm])
            )
            if curr_value > max_val:
                max_val = curr_value
                max_ind = arm
        return max_ind
