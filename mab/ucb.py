""" Upper Confidence Boundary1 Muli-armed banded """
from math import log, sqrt
from mab.mab import MAB


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

    version_ids (list): list of version ids. 
    active_arms set: 
        set of indexes of active arms

    Methods:
    -----------
    All the methods from MAB plus

    select_arm()
        select index of arm to chose next (the core of the algorythm)

    """
    @property
    def name(self) -> str:
        """Name of the algorythm (depends on parameters)

        Returns:
            str: name of the algorythm
        """
        return "UCB1"

    @property
    def marketing_name(self) -> str:
        """High level produnction name"""
        return "Custom solution - 4"

    def select_arm(self) -> int:
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
