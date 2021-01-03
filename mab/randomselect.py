import random
from .mab import MAB


class RandomSelect(MAB):
    """
    Multiarm Bandint that randomly select arm

    ...

    Attributes:
    ----------

    counts : list[int]
        number of times event happend for each arm

    values : list[float]
        total rewards for each arm

    version_ids (list): list of version ids. 

    n_arms : int
        number of arms

    Methods:
    -----------
    All the methods from MAB plus

    select_arm()
        select index of arm to chose next (the core of the algorythm)

    """

    def __init__(
        self, counts=None, values=None, n_arms=None, version_ids=None, active_arms=None
    ):
        """
        Args:
            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)
            version_ids (list): list of version ids. 
                    Defaults to list of indexes as strings
        """
        super().__init__(counts, values, n_arms, version_ids, active_arms)

    @property
    def name(self):
        """name of the algorithm

        Returns:
            str: name of the algorithm
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

        return random.sample(self.active_arms, 1)[0]
