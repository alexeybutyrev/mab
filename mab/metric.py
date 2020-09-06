

class Metric():

    @staticmethod
    def accuracy(best_arm, times, chosen_arms, n_sims):
        accuracy = [0] * (max(times) + 1)
        for i in range(len(chosen_arms)):
            accuracy[times[i]] += int(chosen_arms[i] == best_arm)
        return [a / n_sims for a in accuracy]

    @staticmethod
    def average_reward(times, rewards, n_sims):
        accuracy = [0.0] * (max(times) + 1)
        for i in range(len(rewards)):
            accuracy[times[i]] += rewards[i]
        return [a * 1.0 / n_sims for a in accuracy]

    @staticmethod
    def cumulative_reward(times, cumulative_reward, n_sims):
        accuracy = [0.0] * (max(times) + 1)
        for i in range(len(cumulative_reward)):
            accuracy[times[i]] += cumulative_reward[i]
        return [a / n_sims for a in accuracy]
