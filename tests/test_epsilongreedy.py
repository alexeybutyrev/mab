from mab.epsilongreedy import EpsilonGreedy
import pytest


@pytest.fixture
def model():
    return EpsilonGreedy(0.1, [10, 20], [0.1, 0.5])


@pytest.fixture
def model_added_weakness():
    return EpsilonGreedy(n_arms=10, weakness_mult=0.9)


def test_type_check(model):
    assert isinstance(model, EpsilonGreedy)


def test_name(model):
    assert model.name == "EpsilonGreedy - 0.1"


def test_epsilon_check(model):
    assert model.epsilon == 0.1


def test_weakness(model_added_weakness):
    model_added_weakness.select_arm()
    return model_added_weakness.epsilon == 0.9
