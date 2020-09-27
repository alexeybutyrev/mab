import random
from .mab import MAB


class RandomSelect(MAB):
    """
    Mulitarm Bandint that randomly select arm

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
        """name of the algorythm

        Returns:
            str: name of the algorythm
        """
        return "RandomSelect"

    @property
    def marketing_name(self):
        """High level produnction name"""
        return "A/B Testing"

    def select_arm(self):
        """Randomly select next arm

        Returns:
            int: return random index of the next arm to select
        """
        return random.randint(0, self.n_arms - 1)
