import random
from .mab import MAB
from random import choices
from math import exp


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

    Methods:
    -----------
    All the methods from MAB plus

    select_arm()
        select index of arm to chose next (the core of the algorythm)
    """

    def __init__(self, temperature=0.1, counts=None, values=None, n_arms=None):
        """
        Args:
            tepmerature (float, optional): control paramter for select with proportional to the rewards
                                       Defaults to 1.0.
            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)
        """

        super().__init__(counts, values, n_arms)
        self.temperature = temperature  # parameter of the algorythm

    @property
    def name(self):
        """Name of the algorythm (depends on parameters)

        Returns:
            str: name of the algorythm
        """
        return "Softmax. T=" + str(self.temperature)

    @property
    def marketing_name(self):
        """High level produnction name"""
        return "Custom solution - 2"

    def select_arm(self):
        """Softmax algorythm implementaion

        Returns:
            int: arm to select next
        """
        # update epsilon if weaknes multipler was set
        probs = [exp(v / self.temperature) for v in self.values]
        scale_denomiator = sum(probs)
        probs = [p / scale_denomiator for p in probs]

        return choices(range(self.n_arms), weights=probs)[0]
