"""
    Thompson Sampling Muli-armed banded with Betta Distribution
"""
from math import inf
from typing import List, Set
from numpy.random import beta as beta_distribution
from mab.mab import MAB


class BetaTS(MAB):
    """
    Thompson Sampling Muli-armed banded with Betta Distribution

    ...

    Attributes:
    ----------

    alpha: list[int],
        alpha paramter for each arm

    beta: list[int],
        beta paramter for each arm

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
    reset()
        resets MAB to inital state

    select_arm()
        select index of arm to chose next (the core of the algorythm)

    update(chosen_arm, reward)
        updated chosen arm with the recieved reward
    
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        alpha: List[int] = None,
        beta: List[int] = None,
        counts: List[int] = None,
        values: List[float] = None,
        n_arms: int = None,
        version_ids: List[str] = None,
        active_arms: Set[int] = None,
    ):
        """[summary]

        Args:
            alpha (list, optional): alpha parameter for each arm. Defaults to list of ones

            beta (list, optional):  beta parameter for each arm. Defaults to list of ones

            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)
            
            version_ids (list): list of version ids. 
                                Defaults to list of indexes as strings

            active_arms (set): list with indexes of active versions. 
                When it's none it's set as all the versions
        """
        super().__init__(counts, values, n_arms, version_ids, active_arms)
        if alpha is None:
            alpha = [1] * self.n_arms

        if beta is None:
            beta = [1] * self.n_arms

        self.alpha = alpha
        self.beta = beta

        self.__init_alpha = alpha[:]
        self.__init_beta = beta[:]

    @property
    def name(self) -> str:
        """Name of the algorithm

        Returns:
            str: name of the algorithm
        """
        return "BetaTS"

    @property
    def marketing_name(self) -> str:
        """High level produnction name"""
        return "Custom Solution"

    def select_arm(self) -> int:
        """Thompson Sampling Algorithm implementation

        Returns:
            int: arm to select next
        """
        mx_ = -inf
        selected_arm = 0
        for arm in range(self.n_arms):
            if arm not in self.active_arms:
                tetta = beta_distribution(self.alpha[arm], self.beta[arm])
                if mx_ < tetta:
                    mx_ = tetta
                    selected_arm = arm

        return selected_arm

    def update(self, chosen_arm, reward):
        """Update paramters of the algorithm

        Args:
            chosen_arm (int): arm that received the reward
            reward (int): value of reward
        """
        super().update(chosen_arm, reward)
        self.alpha[chosen_arm] += int(reward)
        self.beta[chosen_arm] += int(1 - reward)

    def reset(self):
        """Reset the Algorithm to the initial state"""
        super().reset()
        self.alpha = self.__init_alpha[:]
        self.beta = self.__init_beta[:]
