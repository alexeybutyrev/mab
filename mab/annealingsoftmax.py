"""Annealing Softmax Multi-arms bandit algorithm
       The idea is to decrease the temerature paramters depending on time
"""
from math import log
from mab.softmax import Softmax


class AnnealingSoftmax(Softmax):
    """Annealing Softmax Multi-arms bandit algorithm
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

    version_ids : list
        list of version ids
    
    temperature : float
        Softmax parameter. Reccomended not to change
    
    active_arms : set
            set of indexes of active arms

    Methods:
    -----------
    All the methods from MAB plus

    select_arm()
        select index of arm to chose next (the core of the algorithm)
    """

    _EPSILON = 0.0000001

    @property
    def name(self) -> str:
        """Name of the algorithm (depends on parameters)

        Returns:
            str: name of the algorithm
        """
        return "AnnealingSoftmax"

    @property
    def marketing_name(self) -> str:
        """High level produnction name"""
        return "Custom solution - 3"

    def select_arm(self):
        """Anearing Softmax algorithm implementation

        Returns:
            int: arm to select next
        """
        temp = 1
        for arm in self.active_arms:
            temp += self.counts[arm] + 1
        self.temperature = 1.0 / log(temp + self._EPSILON)
        # update epsilon if weaknes multipler was set
        return super().select_arm()
