from .mab import MAB
from numpy.random import beta as beta_distribution
from math import inf


class BetaTS(MAB):
    def __init__(self, alpha=None, beta=None, counts=None, values=None, n_arms=None):
        super().__init__(counts, values, n_arms)
        if alpha is None:
            alpha = [1] * self.n_arms

        if beta is None:
            beta = [1] * self.n_arms

        self.alpha = alpha
        self.beta = beta

        self.init_alpha = self.alpha
        self.init_beta = self.beta

    @property
    def name(self):
        return "BetaTS"

    def select_arm(self):

        mx_ = -inf
        selected_arm = 0
        for arm in range(self.n_arms):
            tetta = beta_distribution(self.alpha[arm], self.beta[arm])
            if mx_ < tetta:
                mx_ = tetta
                selected_arm = arm

        return selected_arm

    def update(self, chosen_arm, reward):
        super().update(chosen_arm, reward)
        self.alpha[chosen_arm] += int(reward)
        self.beta[chosen_arm] += int(1 - reward)

    def reset(self):
        super().reset
        self.alpha = self.init_alpha
        self.beta = self.init_beta
