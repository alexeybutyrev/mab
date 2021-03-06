from .mab import MAB
import random


class AB(MAB):
    """AB testing Class for Multiarm Bandit Application

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

    active_arms : set
        set of indexes of active arms

    Methods:
    -----------
    All the methods from MAB plus

    select_arm()
        select arm one by one sequentially

    """

    def __init__(
        self,
        counts=None,
        values=None,
        n_arms=None,
        version_ids=None,
        current_arm=0,
        active_arms=None,
    ):
        """
        Args:
            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)
            
            version_ids (list): list of version ids. Defaults to list of indexes as strings
            current_arm (int): Index of current arm to call. Defaults to 0
            active_arms (set): set of indexes of active arms
        """
        super().__init__(counts, values, n_arms, version_ids, active_arms)

        self.current_arm = current_arm

    @property
    def name(self):
        """name of the algorythm

        Returns:
            str: name of the algorythm
        """
        return "AB-test"

    @property
    def marketing_name(self):
        """High level produnction name"""
        return "One by one A/B"

    def select_arm(self):
        """Select next arm one by one

        Returns:
            int: index of the next arm to select following to the previous arm
        """
        current_arm = self.current_arm
        # switch arm to the next position

        if self.current_arm == self.n_arms - 1:
            self.current_arm = 0
        else:
            self.current_arm += 1

        while self.current_arm not in self.active_arms:
            if self.current_arm == self.n_arms - 1:
                self.current_arm = 0
            else:
                self.current_arm += 1
        # return the arm before
        return current_arm

    def reset(self):
        """Reset the algorithm to the initial state"""
        super(AB, self).reset()
        self.current_arm = 0
