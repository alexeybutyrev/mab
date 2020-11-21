class MAB:
    """
    Mulitarm Bandint base Class

    ...

    Attributes:
    ----------

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

    def __init__(self, counts=None, values=None, n_arms=None):
        """
        Args:
            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)
        """
        if counts is None:
            # set up with zeroes if not defined
            assert n_arms is not None
            counts = [0] * n_arms
            values = [0.0] * n_arms
        else:
            if n_arms is not None:
                assert n_arms == len(counts)

        self.n_arms = len(counts)
        self.counts = counts  # number of counts chose for each arm
        self.values = values  # success rate for each arm

        # we need save start values for reset calls
        self.init_counts = counts[:]
        self.init_values = values[:]

    def __str__(self):
        return str(self.__class__.__name__)

    def reset(self):
        """Reset MAB. Sets counts and values to the inital state"""

        self.counts = self.init_counts[:]
        self.values = self.init_values[:]

    def select_arm(self):
        """Select Arm of MAB:
        returns index of the arms
        must be chosed by algorythm
        """
        pass

    def update(self, chosen_arm, reward):
        """Update chosen arm

        Args:
            chosen_arm (int): arm index
            reward (float): reward
        """
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        self.values[chosen_arm] = ((n - 1) / n) * self.values[chosen_arm] + reward / n

    def compare_to_ab(self):
        """Compare collected rewards agains potential AB test ones
           ## TODO run it on fly when we're updating rewards now the operation in O(narms) the other case would be O(1)
        """

        # AB_rewards 2 cases n/2 * (rewards_1/counts_1) + n/2 * (rewards_2/counts_2) which is euqal
        # AB_rewards = n/2 (rewards_1/counts_1 + rewards_2/counts_2 )
        # rewards_1/counts_1 == values_1
        # below is the caclulation of the second multiplier
        ab_rewards = 0
        total_rewards = 0
        for i in range(self.n_arms):
            ab_rewards += self.values[i]
            total_rewards += self.values[i] * self.counts[i]

        # multiply result // n_arms. // operator to make it as integer for vis purposes
        ab_rewards *= sum(self.counts) // self.n_arms

        return total_rewards - ab_rewards
