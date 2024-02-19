"""
    Multiarm Bandint that randomly select arm
"""

import random
from mab.mab import MAB


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

    @property
    def name(self) -> str:
        """name of the algorithm

        Returns:
            str: name of the algorithm
        """
        return "RandomSelect"

    @property
    def marketing_name(self) -> str:
        """High level produnction name"""
        return "A/B Testing"

    def select_arm(self) -> int:
        """Randomly select next arm

        Returns:
            int: return random index of the next arm to select
        """

        return random.sample(self.active_arms, 1)[0]
