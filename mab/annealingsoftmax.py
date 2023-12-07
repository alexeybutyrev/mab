from mab.softmax import Softmax
from math import log
from typing import List, Set


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

    def __init__(
        self,
        counts: List[int] = None,
        values: List[float] = None,
        n_arms: int = None,
        version_ids: List[str] = None,
        active_arms: Set[int] = None,
        temperature: float = 1.0,
    ):
        """
        Args:
            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)
            version_ids (list): list of version ids. Defaults to list of indexes as strings
            temperature (float): Softmax parameter. Reccomended not to change. Defaults to 1.0
            active_arms (set): set of indexes of active arms
        """
        super().__init__(temperature, counts, values, n_arms, version_ids, active_arms)

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
        t = 1
        for a in self.active_arms:
            t += self.counts[a] + 1
        self.temperature = 1.0 / log(t + 0.0000001)
        # update epsilon if weaknes multipler was set
        return super(AnnealingSoftmax, self).select_arm()
