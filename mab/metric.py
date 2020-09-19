class Metric:
    """
    Metrics for measuring MAB (Multi-armed Bandit Algorythm) productivity

    ...

    Methods:
    -----------
    accuracy(best_arm, times, chosen_arms, n_sims)
        Returns the number of times the best arm was chosen devided by the number of simulations

    average_reward(times, rewards, n_sims)
        Average reward per simulateion for each timestamp

    cumulative_reward(times, cumulative_reward, n_sims)
        Cumulative rewards for each timestamp

    """

    @staticmethod
    def accuracy(best_arm, times, chosen_arms, n_sims):
        """Metric for the frequency of the the arm with the most probable reward at the each timestamp

        Args:
            best_arm (int): The index of arm with the most probable reward
            times (list): indexes for each simulation
            chosen_arms (list): indexes
            n_sims (int): number of simulations

        Returns:
            list: the number of times the best arm was chosen devided by the number of simulations
        """
        accuracy = [0] * (max(times) + 1)
        n_times = len(times)
        for i in range(n_times):
            accuracy[times[i]] += int(chosen_arms[i] == best_arm)
        return [a / n_sims for a in accuracy]

    @staticmethod
    def average_reward(times, rewards, n_sims):
        """Average reward by simulation at each timestamp

        Args:
            times (list): indexes for each simulation
            rewards (list): rewards
            n_sims (int): number of simulations

        Returns:
            list: total number rewards devied by total number of simulations
        """

        accuracy = [0.0] * (max(times) + 1)
        for i in range(len(rewards)):
            accuracy[times[i]] += rewards[i]
        return [a * 1.0 / n_sims for a in accuracy]

    @staticmethod
    def cumulative_reward(times, cumulative_reward, n_sims):
        """Cumulative rewards devided by number of simulations

        Args:
            times (list): indexes for each simulation
            cumulative_reward (list): cumulative rewards
            n_sims (int): number of simulations

        Returns:
            list: cumulative rewards devided by number of simulations
        """
        accuracy = [0.0] * (max(times) + 1)
        for i in range(len(cumulative_reward)):
            accuracy[times[i]] += cumulative_reward[i]
        return [a / n_sims for a in accuracy]
