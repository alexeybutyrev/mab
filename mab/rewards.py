"""Bernoulli distribution Bandit Arm
    Randomly give reward with probability p
"""
# pylint: disable=too-few-public-methods
import random


class BernoulliArm:
    """Bernoulli distribution Bandit Arm
    Randomly give reward with probability p
    ...

    Attributes:
    ----------

    prob : float
        probablity of the reward

    Methods:
    -----------
    draw()
        returns reward

    """

    def __init__(self, prob: float, seed: int = 30):
        """
        Args:
            prob (float): probabilty of choosing arm [0,1]
        """
        random.seed(seed)
        self.prob = prob
        assert 0 <= prob <= 1

    def draw(self) -> float:
        """Randomly return reward with set probablity

        Returns:
            float [0.0, 1.0]: reward
        """
        if random.random() > self.prob:
            return 0.0

        return 1.0


class UniformArm:
    """Bernoulli distribution Bandit Arm
    Randomly give reward with probability p
    ...

    Attributes:
    ----------

    lower_bound : float
        lower bound for reward

    upper_bound : float
        upper bound for reward

    Methods:
    -----------
    draw()
        returns reward

    """

    def __init__(self, lower_bound: float = 0.0, upper_bound: float = 1.0):
        """
        Args:
            lower_bound (float, optional): lower bound for reward. Defaults to 0.0.
            b (float, optional): upper bound for reward. Defaults to 1.0.
        """
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def draw(self) -> float:
        """Randomly return reward as uniform distribution

        Returns:
            float: reward between a and b
        """
        return random.uniform(self.lower_bound, self.upper_bound)
