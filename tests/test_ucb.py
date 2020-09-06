from mab.ucb import UCB
import pytest


@pytest.fixture
def model():
    return UCB([0, 20], [0.1, 0.5])


def test_type(model):
    assert isinstance(model, UCB)


def test_name(model):
    assert model.name == "UCB"


def test_select_arm(model):
    return model.select_arm() == 0
