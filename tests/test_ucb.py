from mab.ucb import UCB1
import pytest


@pytest.fixture
def model():
    return UCB1([0, 20], [0.1, 0.5])


def test_type(model):
    assert isinstance(model, UCB1)


def test_name(model):
    assert model.name == "UCB1"


def test_select_arm(model):
    assert model.select_arm() == 0
