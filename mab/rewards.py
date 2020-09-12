import random


class BernoulliArm:
    """Bernoulli distribution Bandit Arm
    Randomly give reward with probability p
    """

    def __init__(self, p):
        """
        Args:
            p (float): probabilty of choosing arm [0,1]
        """
        self.p = p
        assert p >= 0 and p <= 1

    def draw(self):
        if random.random() > self.p:
            return 0.0
        else:
            return 1.0


class UniformArm:
    """Uniform distribution Bandit Arm
    Randomly give reward between a anb b
    """

    def __init__(self, a=0.0, b=1.0):
        """
        Args:
            a (float, optional): [description]. Defaults to 0.0.
            b (float, optional): [description]. Defaults to 1.0.
        """
        self.a = a
        self.b = b

    def draw(self):
        return random.uniform(self.a, self.b)
