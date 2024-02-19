from mab import enums
from typing import List
from dataclasses import dataclass, field


@dataclass
class ExperimentRewards:
    """ Rewards results for the experiment """

    times: List[int]
    possible_rewards: List[int]
    rewards: List[int]
    cumulative_rewards: List[int] = field(default=None)
    n_sims: int = field(default=1)


def accuracy(experiment_rewards: ExperimentRewards) -> List[float]:
    """Metric for the frequency of the the arm with the most probable reward at the each timestamp

    Args:
        ExperimentRewards

    Returns:
        list: the number of times the best arm was chosen divided by the number of simulations
    """

    accuracy = []
    for i in range(len(experiment_rewards.rewards)):
        if experiment_rewards.possible_rewards[i]:
            accuracy.append(
                experiment_rewards.rewards[i] / experiment_rewards.possible_rewards[i]
            )

    return [a / experiment_rewards.n_sims for a in accuracy]


def cumulative_reward(experiment_rewards: ExperimentRewards) -> List[float]:
    """Cumulative rewards divided by number of simulations

    Args:
        ExperimentRewards

    Returns:
        list: cumulative rewards devided by number of simulations
    """
    accuracy = [0.0] * (max(experiment_rewards.times) + 1)
    for i in range(len(experiment_rewards.cumulative_rewards)):
        accuracy[experiment_rewards.times[i]] += experiment_rewards.cumulative_rewards[
            i
        ]
    return [a / experiment_rewards.n_sims for a in accuracy]


def regret(experiment_rewards: ExperimentRewards) -> List[float]:
    """Difference between expected reward and recieved

    Args:
        ExperimentRewards

    Returns:
        list: the number of times the best arm was chosen devided by the number of simulations
    """
    accuracy = [0] * (max(experiment_rewards.times) + 1)
    counts = [0] * (max(experiment_rewards.times) + 1)
    n_times = len(experiment_rewards.times)

    for i in range(n_times):
        if experiment_rewards.possible_rewards[i]:
            accuracy[experiment_rewards.times[i]] += int(
                experiment_rewards.possible_rewards[i] - experiment_rewards.rewards[i]
            )
            counts[experiment_rewards.times[i]] += 1

    for i in range(max(experiment_rewards.times) + 1):
        accuracy[i] /= max(1, counts[i])
    return [a / experiment_rewards.n_sims for a in accuracy]


def average_reward(experiment_rewards: ExperimentRewards) -> List[float]:
    """Average reward by simulation at each timestamp

    Args:
        ExperimentRewards

    Returns:
        list: total number rewards devied by total number of simulations
    """

    accuracy = [0.0] * (max(experiment_rewards.times) + 1)
    for i in range(len(experiment_rewards.rewards)):
        if experiment_rewards.possible_rewards[i]:
            accuracy[experiment_rewards.times[i]] = (
                experiment_rewards.rewards[i] / experiment_rewards.possible_rewards[i]
            )

    return [a / experiment_rewards.n_sims for a in accuracy]


metrics_mapping = {
    enums.ACCURACY: accuracy,
    enums.AVERAGE_REWARD: average_reward,
    enums.CUMULATIVE_REWARD: cumulative_reward,
    enums.REGRET: regret,
}
