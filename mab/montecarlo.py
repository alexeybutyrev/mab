from copy import deepcopy
from collections import defaultdict


class Simulation:
    """
    Simulation - class containing simulation attributues and results

    ...

    Attributes:
    ----------

    algorytm: MAB,
        Multiarm Bandit algorythm

    n_sims : int
        Number of simulations

    horizon : int
        Maximum time

    Methods:
    -----------
    All the methods from MAB plus

    reset()
        reset the algorythm to inital state
    """

    def __init__(self, algorytm, n_sims, horizon, name=None):
        """
        Args:
            algorytm(MAB): Multiarm Bandit algorythm
            n_sims(int): Number of simulations
            horizon(int): Maximum time
            name(str, optional): name of the simualtion
        """
        self.n_sims = n_sims
        self.horizon = horizon
        self.algorytm = algorytm
        self.chosen_arms = [0.0 for i in range(n_sims * horizon)]
        self.rewards = [0.0 for i in range(n_sims * horizon)]
        self.cumulative_rewards = [0.0 for i in range(n_sims * horizon)]
        self.possible_rewards = [0.0 for i in range(n_sims * horizon)]
        self.marketing_name = algorytm.marketing_name
        if name is None:
            self.name = algorytm.name

        self.metrics = defaultdict(list)

    def reset(self):
        self.algorytm.reset()


class MonteCarloSimulation:
    """
    MonteCarloSimulation
    Monte Carlo Simulation of differnt Multi-armed Bandit algorythms

    ...

    Attributes:
    ----------

    algs: list,
        list of Multiarm Bandit algorythms

    arms: Arm,
        Rewards Simulation

    n_sims : int
        Number of simulations

    horizon : int
        Maximum time

    Methods:
    -----------
    All the methods from MAB plus

    run()
        Run simulations
    calculate_metrics()
        Calculate metrics for existent simualtions
    """

    def __init__(self, algs, arms, n_sims, horizon):
        """
        Args:
            algs(list): list of Multiarm Bandit algorythms
            n_sims(int): Number of simulations
            horizon(int): Maximum time
        """
        self.n_sims = n_sims
        self.horizon = horizon

        self.arms = arms

        self.sim_nums = [0.0 for i in range(n_sims * horizon)]
        self.times = [0.0 for i in range(n_sims * horizon)]

        self.simulations = []
        for alg in algs:
            self.simulations.append(Simulation(alg, n_sims, horizon))

    def __getitem__(self, ind):
        """get simulation by index

        Args:
            ind (int): index of the simulation

        Returns:
            Simulation: simulation object
        """
        return self.simulations[ind]

    def run(self):
        """Run simulations"""
        for sim in range(self.n_sims):
            for s in self.simulations:
                s.reset()

                for t in range(self.horizon):
                    for s in self.simulations:
                        index = sim * self.horizon + t
                        self.sim_nums[index] = sim
                        self.times[index] = t

                        chosen_arm = s.algorytm.select_arm()
                        s.chosen_arms[index] = chosen_arm

                        # check out if any rewards for the current time and simulation
                        # save 0 in possible rewards and 1 otherwise
                        all_rewards = list(map(lambda x: x.draw(), self.arms))
                        s.possible_rewards[index] = int(sum(all_rewards) > 0)

                        reward = all_rewards[chosen_arm]
                        s.rewards[index] = reward

                        if t == 0:
                            s.cumulative_rewards[index] = reward
                        else:
                            s.cumulative_rewards[index] = (
                                s.cumulative_rewards[index - 1] + reward
                            )

                        s.algorytm.update(chosen_arm, reward)

    def calculate_metrics(
        self,
        Metric,
        metrics=["accuracy", "average_reward", "cumulative_reward", "regret"],
    ):
        """Calculate metrics for existent simualtions

        Args:
            Metric (Metric): object with metrics calculations
            metrics (list, optional): [description]. List of metrics to make calculations ["accuracy", "average_reward", "cumulative_reward", "regret"].
        """
        for s in self.simulations:
            if "accuracy" in metrics:
                s.metrics["accuracy"] = Metric.accuracy(
                    self.times, s.possible_rewards, s.rewards, self.n_sims
                )

            if "average_reward" in metrics:
                s.metrics["average_reward"] = Metric.average_reward(
                    self.times, s.possible_rewards, s.rewards, self.n_sims
                )

            if "cumulative_reward" in metrics:
                s.metrics["cumulative_reward"] = Metric.cumulative_reward(
                    self.times, s.cumulative_rewards, self.n_sims
                )

            if "regret" in metrics:
                s.metrics["regret"] = Metric.regret(
                    self.times, s.possible_rewards, s.rewards, self.n_sims
                )
