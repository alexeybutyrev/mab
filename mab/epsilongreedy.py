import random
from .mab import MAB


class EpsilonGreedy(MAB):
    """
    EpsilonGreedy Muli-armed banded

    ...

    Attributes:
    ----------

    epsilon: float,
        probablity of chosing random arm. Otherwise we choose the most profitable one

    counts : list[int]
        number of times event happend for each arm

    values : list[float]
        total rewards for each arm

    n_arms : int
        number of arms

    weakness_mult: float
        multiplier fore reduction epsilon at every timestep

    Methods:
    -----------
    All the methods from MAB plus

    reset()
        resets MAB to inital state

    select_arm()
        select index of arm to chose next (the core of the algorythm)

    update(chosen_arm, reward)
        updated chosen arm with the recieved reward
    """

    def __init__(
        self, epsilon=1.0, counts=None, values=None, n_arms=None, weakness_mult=None
    ):
        """
        Args:
            epsilon (float, optional): probablity of chosing random arm. Otherwise we choose the most profitable one
                                       Defaults to 1.0.
            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)

        """
        super().__init__(counts, values, n_arms)
        self.epsilon = epsilon  # probablity of choosing random arm
        self.weakness_mult = None

        if weakness_mult is not None:
            self.weakness_mult = weakness_mult
            self.epsilon = 1.0
        self.init_epsilon = self.epsilon

    @property
    def name(self):
        """Name of the algorythm (depends on parameters)

        Returns:
            str: name of the algorythm
        """
        if self.weakness_mult is None:
            return "EpsilonGreedy - " + str(self.epsilon)
        else:
            return "EpsilonWeakGreedy - " + str(self.weakness_mult)

    @property
    def marketing_name(self):
        """High level produnction name"""
        return "PM's solution"

    def select_arm(self):
        """EpsilonGreedy algorythm implementaion

        Returns:
            int: arm to select next
        """
        if self.weakness_mult is not None:
            self.epsilon *= self.weakness_mult

        def argmax(x):
            return max(enumerate(x), key=lambda x: x[1])[0]

        if random.random() > self.epsilon:
            return argmax(self.values)
        else:
            return random.randint(0, self.n_arms - 1)

    def reset(self):
        """Reset the Algorythm to the initial state"""
        super().reset()
        self.epsilon = self.init_epsilon
