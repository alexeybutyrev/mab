from mab.metric import Metric


def test_accuracy():
    assert [0.5, 1.0] == Metric.accuracy(1, [0, 0, 1, 1], [0, 1, 1, 1], 2)


def test_average_reward():
    assert [0.5, 1.0] == Metric.average_reward([0, 0, 1, 1], [0, 1, 1, 1], 2)


def test_cumulative_reward():
    assert [0.5, 1.0] == Metric.cumulative_reward([0, 0, 1, 1], [0, 1, 1, 1], 2)
