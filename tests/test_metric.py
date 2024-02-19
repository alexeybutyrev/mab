# from mab.metric import Metric

import pytest
from mab.metric import MetricsCalculator, ExperimentRewards

# Sample data for testing
times = [1, 2, 3, 4]
possible_rewards = [10, 20, 30, 40]
rewards = [5, 10, 15, 20]
cumulative_rewards = [50, 100, 150, 200]
n_sims = 2


@pytest.fixture
def experiment_rewards():
    return ExperimentRewards(
        times=times,
        possible_rewards=possible_rewards,
        rewards=rewards,
        cumulative_rewards=cumulative_rewards,
        n_sims=n_sims,
    )


def test_calculate_accuracy(experiment_rewards):
    expected_accuracy = [
        0.25,
        0.25,
        0.25,
        0.25,
    ]  # Calculate expected accuracy based on sample data
    accuracy = MetricsCalculator.calculate_accuracy(experiment_rewards)
    assert accuracy == expected_accuracy


def test_calculate_cumulative_reward(experiment_rewards):
    expected_cumulative_reward = [
        0.0,
        25.0,
        50.0,
        75.0,
        100.0,
    ]  # Calculate expected cumulative reward based on sample data
    cumulative_reward = MetricsCalculator.calculate_cumulative_reward(
        experiment_rewards
    )
    assert cumulative_reward == expected_cumulative_reward


def test_calculate_regret(experiment_rewards):
    expected_regret = [
        0,
        2.5,
        5.0,
        7.5,
        10.0,
    ]  # Calculate expected regret based on sample data
    regret = MetricsCalculator.calculate_regret(experiment_rewards)
    assert regret == expected_regret


def test_calculate_average_reward(experiment_rewards):
    expected_average_reward = [
        0.0,
        0.25,
        0.25,
        0.25,
        0.25,
    ]  # Calculate expected average reward based on sample data
    average_reward = MetricsCalculator.calculate_average_reward(experiment_rewards)
    assert average_reward == expected_average_reward
