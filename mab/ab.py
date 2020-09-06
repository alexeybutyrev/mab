from .mab import MAB
import random


class AB(MAB):
    def __init__(self, counts=None, values=None, n_arms=None):
        super().__init__(counts, values, n_arms)
        self.current_arm = 0

    @property
    def name(self):
        return "AB-test"

    def select_arm(self):
        current_arm = self.current_arm
        # switch arm to the next position
        if self.current_arm == self.n_arms - 1:
            self.current_arm = 0
        else:
            self.current_arm += 1

        # return the arm before
        return current_arm

    def reset(self):
        super(AB, self).reset()
        self.current_arm = 0
