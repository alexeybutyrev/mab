from mab.mab import MAB
import pytest


@pytest.fixture
def model():
    return MAB([10, 20], [0.1, 0.5])


def test_type_check(model):
    assert isinstance(model, MAB)


def test_lenghts_check(model):
    assert len(model.counts) == len(model.values)


def test_narms_check(model):
    assert model.n_arms == len(model.values)


def test_reset_check(model):
    model.reset()
    assert sum(model.counts) == 30
    assert sum(model.values) == 0.6
