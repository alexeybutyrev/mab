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
    def accuracy(times, possible_rewards, rewards, n_sims):
        """Metric for the frequency of the the arm with the most probable reward at the each timestamp

        Args:
            times (list): indexes for each simulation
            possible_rewards (list): list if reward was
            rewards (list): rewards
            n_sims (int): number of simulations

        Returns:
            list: the number of times the best arm was chosen devided by the number of simulations
        """

        accuracy = [0] * (max(times) + 1)
        n_times = len(times)
        for i in range(n_times):
            accuracy[times[i]] += int(possible_rewards[i] == rewards[i])
        return [a / n_sims for a in accuracy]

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

    @staticmethod
    def regret(times, possible_rewards, rewards, n_sims):
        """Difference between expected reward and recieved

        Args:
            times (list): indexes for each simulation
            possible_rewards (list): list if reward was
            rewards (list): rewards
            n_sims (int): number of simulations

        Returns:
            list: the number of times the best arm was chosen devided by the number of simulations
        """
        accuracy = [0] * (max(times) + 1)
        counts = [0] * (max(times) + 1)
        n_times = len(times)

        for i in range(n_times):
            if possible_rewards[i]:
                accuracy[times[i]] += int(possible_rewards[i] - rewards[i])
                counts[times[i]] += 1

        for i in range(max(times) + 1):
            accuracy[i] /= max(1, counts[i])
        return accuracy

    @staticmethod
    def average_reward(times, possible_rewards, rewards, n_sims):
        """Average reward by simulation at each timestamp

        Args:
            times (list): indexes for each simulation
            possible_rewards (list): list if reward was
            rewards (list): rewards
            n_sims (int): number of simulations

        Returns:
            list: total number rewards devied by total number of simulations
        """

        accuracy = [0.0] * (max(times) + 1)
        n_rewards = [0.0] * (max(times) + 1)
        for i in range(len(rewards)):
            if possible_rewards[i]:
                accuracy[times[i]] += rewards[i]
                n_rewards[times[i]] += 1

        total_rewards = sum(accuracy)
        total_reward_times = max(1, sum(n_rewards))

        return [total_rewards / total_reward_times] * (max(times) + 1)