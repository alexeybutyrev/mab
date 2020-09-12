from mab.bernoulliarm import BernoulliArm
import pytest


@pytest.fixture
def model():
    return BernoulliArm(0.1)


def test_type_check(model):
    assert isinstance(model, BernoulliArm)


def test_draw(model):
    assert model.draw() in [0.0, 1.0]
