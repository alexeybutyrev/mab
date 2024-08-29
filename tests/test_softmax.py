from mab.softmax import Softmax
import pytest


@pytest.fixture
def model():
    return Softmax([10, 20], [0.1, 0.5], temperature=0.1)


def test_type(model):
    assert isinstance(model, Softmax)


def test_name(model):
    assert model.name == "Softmax. T=0.1"


def test_temperature_check(model):
    assert model.temperature == 0.1


def test_select_arm(model):
    assert model.select_arm() in [0, 1]
