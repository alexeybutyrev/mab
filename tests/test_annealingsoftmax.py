from mab.annealingsoftmax import AnnealingSoftmax
import pytest


@pytest.fixture
def model():
    return AnnealingSoftmax([10, 20], [0.1, 0.5])


def test_type(model):
    assert isinstance(model, AnnealingSoftmax)


def test_name(model):
    assert model.name == "AnnealingSoftmax"


def test_select_arm(model):
    return model.select_arm() in [0, 1]
