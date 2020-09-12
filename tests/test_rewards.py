from mab.rewards import BernoulliArm
import pytest
from mab.rewards import UniformArm


@pytest.fixture
def model():
    return BernoulliArm(0.1)


def test_type_check(model):
    assert isinstance(model, BernoulliArm)


def test_draw(model):
    assert model.draw() in [0.0, 1.0]


@pytest.fixture
def umodel():
    return UniformArm(0, 100)


def test_utype_check(umodel):
    assert isinstance(umodel, UniformArm)


def test_udraw(umodel):
    reward = umodel.draw()
    assert reward >= 0 and reward <= 100
