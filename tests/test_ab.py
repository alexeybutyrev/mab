from mab.ab import AB
import pytest


@pytest.fixture
def model():
    return AB([10, 20], [0.1, 0.5])


def test_type_check(model):
    assert isinstance(model, AB)


def test_select_arm(model):
    assert model.select_arm() == 0
    assert model.select_arm() == 1
    assert model.select_arm() == 0


def test_reset(model):
    model.reset()
    assert sum(model.counts) == 30
    assert model.current_arm == 0
