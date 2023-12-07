from mab.mab import MAB
from random import choices
from math import exp
from typing import List, Set


class Softmax(MAB):
    """
    Softmax Muli-armed banded

    ...

    Attributes:
    ----------

    temperature: float,
        paramter of the algorythm

    counts : list[int]
        number of times event happend for each arm

    values : list[float]
        total rewards for each arm

    n_arms : int
        number of arms

    version_ids : list
        list of version ids

    active_arms set: 
        set of indexes of active arms
        
    Methods:
    -----------
    All the methods from MAB plus

    select_arm()
        select index of arm to chose next (the core of the algorithm)
    """

    def __init__(
        self,
        temperature: float = 0.1,
        counts: List[int] = None,
        values: List[float] = None,
        n_arms: int = None,
        version_ids: List[str] = None,
        active_arms: Set[int] = None,
    ):
        """
        Args:
            temperature (float, optional): control parameter for select with proportional to the rewards
                                       Defaults to 1.0.
            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)
            version_ids (list): list of version ids. 
                                Defaults to list of indexes as strings
            active_arms (set): set of indexes of active arms
        """

        super().__init__(counts, values, n_arms, version_ids, active_arms)
        self.temperature = temperature  # parameter of the algorithm

    @property
    def name(self) -> str:
        """Name of the algorithm (depends on parameters)

        Returns:
            str: name of the algorithm
        """
        return "Softmax. T=" + str(self.temperature)

    @property
    def marketing_name(self) -> str:
        """High level produnction name"""
        return "Custom solution - 2"

    def select_arm(self) -> int:
        """Softmax algorythm implementaion

        Returns:
            int: arm to select next
        """
        # update epsilon if weaknes multipler was set
        # TODO change logic with active versions
        probs = [exp(v / self.temperature) for v in self.values]
        scale_denomiator = sum(probs)
        probs = [p / scale_denomiator for p in probs]

        return choices(range(self.n_arms), weights=probs)[0]
