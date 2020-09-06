from mab.randomselect import RandomSelect
import pytest


@pytest.fixture
def model():
    return RandomSelect([10, 20], [0.1, 0.5])


def test_type_check(model):
    assert isinstance(model, RandomSelect)


def test_name(model):
    assert model.name == "RandomSelect"


def test_select_arm(model):
    assert model.select_arm() in [0, 1]
