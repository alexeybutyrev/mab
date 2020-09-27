import random
from .mab import MAB
from math import log, sqrt


class UCB1(MAB):
    """
    Upper Confidence Boundary1 Muli-armed banded

    ...

    Attributes:
    ----------

    counts : list[int]
        number of times event happend for each arm

    values : list[float]
        total rewards for each arm

    n_arms : int
        number of arms

    Methods:
    -----------
    All the methods from MAB plus

    select_arm()
        select index of arm to chose next (the core of the algorythm)

    """

    def __init__(self, counts=None, values=None, n_arms=None):
        """
        Args:
            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)

        """
        super().__init__(counts, values, n_arms)

    @property
    def name(self):
        """Name of the algorythm (depends on parameters)

        Returns:
            str: name of the algorythm
        """
        return "UCB1"

    @property
    def marketing_name(self):
        """High level produnction name"""
        return "Custom solution - 4"

    def select_arm(self):
        """Upper Confidence Boundary1 algorythm implementaion

        Returns:
            int: arm to select next
        """

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
