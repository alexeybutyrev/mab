from .mab import MAB
from numpy.random import beta as beta_distribution
from math import inf


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

    Methods:
    -----------
    reset()
        resets MAB to inital state

    select_arm()
        select index of arm to chose next (the core of the algorythm)

    update(chosen_arm, reward)
        updated chosen arm with the recieved reward
    """

    def __init__(self, alpha=None, beta=None, counts=None, values=None, n_arms=None):
        """[summary]

        Args:
            alpha (list, optional): alpha paramter for each arm. Defaults to list of ones

            beta (list, optional):  beta paramter for each arm. Defaults to list of ones

            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)

        """
        super().__init__(counts, values, n_arms)
        if alpha is None:
            alpha = [1] * self.n_arms

        if beta is None:
            beta = [1] * self.n_arms

        self.alpha = alpha
        self.beta = beta

        self.init_alpha = alpha[:]
        self.init_beta = beta[:]

    @property
    def name(self):
        """Name of the algorythm

        Returns:
            str: name of the algorythm
        """
        return "BetaTS"

    @property
    def marketing_name(self):
        """High level produnction name"""
        return "Custom Solution"

    def select_arm(self):
        """Thompson Sampling Algorythm implementaion

        Returns:
            int: arm to select next
        """
        mx_ = -inf
        selected_arm = 0
        for arm in range(self.n_arms):
            tetta = beta_distribution(self.alpha[arm], self.beta[arm])
            if mx_ < tetta:
                mx_ = tetta
                selected_arm = arm

        return selected_arm

    def update(self, chosen_arm, reward):
        """Update paramters of the algorythm

        Args:
            chosen_arm (int): arm that recieved the reward
            reward (int): value of reward
        """
        super().update(chosen_arm, reward)
        self.alpha[chosen_arm] += int(reward)
        self.beta[chosen_arm] += int(1 - reward)

    def reset(self):
        """Reset the Algorythm to the initial state"""
        super().reset
        self.alpha = self.init_alpha[:]
        self.beta = self.init_beta[:]
