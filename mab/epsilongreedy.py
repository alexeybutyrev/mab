"""
    EpsilonGreedy Muli-armed banded
"""

import random
from typing import List, Set
from mab.mab import MAB


class EpsilonGreedy(MAB):
    """
    EpsilonGreedy Muli-armed banded

    ...

    Attributes:
    ----------

    epsilon: float,
        probability of choosing random arm. Otherwise we choose the most profitable one

    counts : list[int]
        number of times event happend for each arm

    values : list[float]
        total rewards for each arm

    n_arms : int
        number of arms

    version_ids (list): list of version ids. 
                        Defaults to list of indexes as strings

    weakness_mult: float
        multiplier fore reduction epsilon at every timestep

    active_arms set: 
        list with indexes of active versions

    Methods:
    -----------
    All the methods from MAB plus

    reset()
        resets MAB to initial state

    select_arm()
        select index of arm to chose next (the core of the algorithm)

    update(chosen_arm, reward)
        updated chosen arm with the received reward
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        epsilon: float = 1.0,
        counts: List[int] = None,
        values: List[float] = None,
        n_arms: int = None,
        version_ids: List[str] = None,
        active_arms: Set[int] = None,
        weakness_mult: float = None,
    ):
        """
        Args:
            epsilon (float, optional): probability of choosing random arm. 
                                Otherwise we choose the most profitable one
                                       Defaults to 1.0.
            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)

            version_ids (list): list of version ids. 
                                Defaults to list of indexes as strings

            weakness_mult (float): Weekness multiplier. 
                The idea is to decrease epsilon by that values 

            active_arms (set): list with indexes of active versions
        """
        super().__init__(counts, values, n_arms, version_ids, active_arms)
        self.epsilon = epsilon  # probablity of choosing random arm
        self.weakness_mult = None

        if weakness_mult is not None:
            self.weakness_mult = weakness_mult
            self.epsilon = 1.0
        self.__init_epsilon = self.epsilon

    @property
    def name(self) -> str:
        """Name of the algorythm (depends on parameters)

        Returns:
            str: name of the algorythm
        """
        if self.weakness_mult is None:
            return "EpsilonGreedy - " + str(self.epsilon)

        return "EpsilonWeakGreedy - " + str(self.weakness_mult)

    @property
    def marketing_name(self) -> str:
        """High level produnction name"""
        return "PM's solution"

    def select_arm(self) -> int:
        """EpsilonGreedy algorythm implementaion

        Returns:
            int: arm to select next
        """
        if self.weakness_mult is not None:
            self.epsilon *= self.weakness_mult

        def argmax(values, active_arms):
            max_val = -1
            ind = 0
            for i, val in enumerate(values):
                if i in active_arms and val > max_val:
                    max_val = val
                    ind = i

            return ind

        if random.random() > self.epsilon:
            return argmax(self.values, self.active_arms)

        return random.sample(self.active_arms, 1)[0]

    def reset(self):
        """Reset the Algorythm to the initial state"""
        super().reset()
        self.epsilon = self.__init_epsilon
