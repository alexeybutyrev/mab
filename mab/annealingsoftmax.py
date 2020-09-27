import random
from .softmax import Softmax
from math import log


class AnnealingSoftmax(Softmax):
    """Anealing Softmax Multi-arms bandit algorythm
       The idea is to decrease the temerature paramters depending on time

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
        super().__init__(1.0, counts, values, n_arms)

    @property
    def name(self):
        """Name of the algorythm (depends on parameters)

        Returns:
            str: name of the algorythm
        """
        return "AnnealingSoftmax"

    @property
    def marketing_name(self):
        """High level produnction name"""
        return "Custom solution - 3"

    def select_arm(self):
        """Anealing Softmax algorythm implementaion

        Returns:
            int: arm to select next
        """
        t = sum(self.counts) + 1
        self.temperature = 1.0 / log(t + 0.0000001)
        # update epsilon if weaknes multipler was set
        return super(AnnealingSoftmax, self).select_arm()
