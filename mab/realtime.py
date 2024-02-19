""" Module for realtime simulation"""
import collections
import random
from mab import metric
from mab.mab import MAB
from mab import enums
from simpy import Environment
from typing import List


class EventsSimulation:
    """
    EventsSimulation - simulation the sequence of the events

    ...

    Attributes:
    ----------

    env: Environment from simpy for simulation

    algorithm: MAB,
        Multiarm Bandit algorithm

    arms: list with Bernoulli arms
    name: None

    Methods:
    -----------
    All the methods from MAB plus

    reset()
        reset the algorithm to initial state
    
    run()
        run simulation
    """

    def __init__(
        self, env: Environment, algorithm: MAB, arms: List[int], name: str = None
    ):
        """
        Args:
            algorithm(MAB): Multiarm Bandit algorithm
            n_sims(int): Number of simulations
            horizon(int): Maximum time
            name(str, optional): name of the simulation
        """
        self.env = env
        self.horizon = 0
        self.algorithm = algorithm
        self.arms = arms

        self.chosen_arms = []
        self.rewards = []
        self.cumulative_rewards = []
        self.possible_rewards = []
        self.marketing_name = algorithm.marketing_name
        if name is None:
            self.name = algorithm.name

        self.metrics = collections.defaultdict(list)
        self.action = env.process(self.run())

    def reset(self):
        self.algorithm.reset()

    def run(self):
        """ Run one simulation

        Args:
            sim (int): [description]
            s (Simulation): [description]
        """
        while True:
            self.horizon += 1

            chosen_arm = self.algorithm.select_arm()
            self.chosen_arms.append(chosen_arm)

            # check out if any rewards for the current time and simulation
            # save 0 in possible rewards and 1 otherwise
            all_rewards = list(map(lambda x: x.draw(), self.arms))
            self.possible_rewards.append(int(sum(all_rewards) > 0))

            reward = all_rewards[chosen_arm]
            self.rewards.append(reward)

            if self.cumulative_rewards:
                self.cumulative_rewards.append(self.cumulative_rewards[-1] + reward)
            else:
                self.cumulative_rewards.append(reward)

            self.algorithm.update(chosen_arm, reward)

            yield self.env.timeout(1)

    def calculate_metrics(
        self, metrics: List[str] = None,
    ):
        """Calculate metrics for existent simulations

            Args:
                metrics (list, optional): [description]. List of metrics to make calculations ["accuracy", "average_reward", "cumulative_reward", "regret"].
            """
        if not metrics:
            metrics = enums.CORE_METRICS
        times = list(range(1, self.horizon + 1))
        if "accuracy" in metrics:
            self.metrics["accuracy"] = metric.accuracy(
                times, self.possible_rewards, self.rewards, 1
            )

        if "average_reward" in metrics:
            self.metrics["average_reward"] = metric.average_reward(
                times, self.possible_rewards, self.rewards, 1
            )

        if "cumulative_reward" in metrics:
            self.metrics["cumulative_reward"] = metric.cumulative_reward(
                times, self.cumulative_rewards, 1
            )

        if "regret" in metrics:
            self.metrics["regret"] = metric.regret(
                times, self.possible_rewards, self.rewards, 1
            )


class UISimulation:
    """
    UISimulation -  Simulation of the UI when random N users (between Nmin and Nmax) come to the UI every minute and do some actions with preset arms (probailties to click on each action)

    ...

    Attributes:
    ----------

    algorithm: MAB,
        Multiarm Bandit algorithm

    n_customers_low : int
        Minimum customers that show at current minute

    n_customers_high : int
        Maximum customers that show at current minute

    Methods:
    -----------
    All the methods from MAB plus

    reset()
        reset the algorithm to initial state
    
    run()
        run simulation
    """

    def __init__(
        self,
        env: Environment,
        algorithm: MAB,
        arms: List[int],
        n_customers_low: int,
        n_customers_high: int,
        name: str = None,
    ):
        """
        Args:
            algorithm(MAB): Multiarm Bandit algorithm
            n_sims(int): Number of simulations
            horizon(int): Maximum time
            name(str, optional): name of the simulation
        """
        self.env = env
        self.horizon = 0
        self.algorithm = algorithm
        self.arms = arms

        self.n_customers_low = n_customers_low
        self.n_customers_high = n_customers_high

        self.chosen_arms = []
        self.rewards = []
        self.cumulative_rewards = []
        self.possible_rewards = []
        self.marketing_name = algorithm.marketing_name

        # rewards difference compring to AB test assuming we don't know the result
        self.rewards_difference_to_ab = []

        if name is None:
            self.name = algorithm.name

        self.metrics = collections.defaultdict(list)
        self.action = env.process(self.run())

    def reset(self):
        self.algorithm.reset()

    def run(self):
        """ Run one simulation

        Args:
            sim (int): [description]
            s (Simulation): [description]
        """
        while True:
            self.horizon += 1
            minute_rewards = 0
            possible_minute_rewards = 0
            for _ in range(random.randint(self.n_customers_low, self.n_customers_high)):
                chosen_arm = self.algorithm.select_arm()
                self.chosen_arms.append(chosen_arm)

                # check out if any rewards for the current time and simulation
                # save 0 in possible rewards and 1 otherwise
                all_rewards = list(map(lambda x: x.draw(), self.arms))
                possible_minute_rewards += int(sum(all_rewards) > 0)

                reward = all_rewards[chosen_arm]
                minute_rewards += reward

                self.algorithm.update(chosen_arm, reward)

            self.possible_rewards.append(possible_minute_rewards)
            self.rewards.append(minute_rewards)

            r = self.algorithm.compare_to_ab()

            self.rewards_difference_to_ab.append(r)
            if self.cumulative_rewards:
                self.cumulative_rewards.append(
                    self.cumulative_rewards[-1] + minute_rewards
                )
            else:
                self.cumulative_rewards.append(minute_rewards)

            yield self.env.timeout(1)

    def calculate_metrics(
        self, metrics: List[str] = None,
    ):
        """Calculate metrics for existent simulations
            Args:
                metrics (list, optional): [description]. List of metrics to make calculations ["accuracy", "average_reward", "cumulative_reward", "regret"].
            """
        if not metrics:
            metrics = enums.CORE_METRICS
        times = list(range(1, self.horizon + 1))

        experiment_rewards = metric.ExperimentRewards(
            times=times,
            possible_rewards=self.possible_rewards,
            rewards=self.rewards,
            cumulative_rewards=self.cumulative_rewards,
        )
        for metric_name in metrics:
            self.metrics[metric_name] = metric.metrics_mapping[metric_name](
                experiment_rewards
            )

        if enums.COMPARE_TO_AB in metrics:
            self.metrics[enums.COMPARE_TO_AB] = self.rewards_difference_to_ab

