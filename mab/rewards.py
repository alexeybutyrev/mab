import random


class BernoulliArm:
    """Bernoulli distribution Bandit Arm
    Randomly give reward with probability p
    ...

    Attributes:
    ----------

    p : float
        probablity of the reward

    Methods:
    -----------
    draw()
        returns reward

    """

    def __init__(self, p):
        """
        Args:
            p (float): probabilty of choosing arm [0,1]
        """
        self.p = p
        assert p >= 0 and p <= 1

    def draw(self):
        """Randomly return reward with set probablity

        Returns:
            float [0.0, 1.0]: reward
        """
        if random.random() > self.p:
            return 0.0
        else:
            return 1.0


class UniformArm:
    """Bernoulli distribution Bandit Arm
    Randomly give reward with probability p
    ...

    Attributes:
    ----------

    a : float
        lower bound for reward

    b : float
        upper bound for reward

    Methods:
    -----------
    draw()
        returns reward

    """

    def __init__(self, a=0.0, b=1.0):
        """
        Args:
            a (float, optional): lower bound for reward. Defaults to 0.0.
            b (float, optional): upper bound for reward. Defaults to 1.0.
        """
        self.a = a
        self.b = b

    def draw(self):
        """Randomly return reward as uniform distribution

        Returns:
            float: reward between a and b
        """
        return random.uniform(self.a, self.b)
