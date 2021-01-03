from mab import betats
from mab.tools import dict2MAB
from mab.ab import AB
from mab.ucb1 import UCB1
from mab.annealingsoftmax import AnnealingSoftmax
from mab.betats import BetaTS
from mab.softmax import Softmax
from mab.epsilongreedy import EpsilonGreedy
from mab.randomselect import RandomSelect


def test_dict2MAB_AB():
    m = AB([10, 20], [0.1, 0.5])
    assert m.counts == [10, 20]
    m.select_arm()
    m.select_arm()
    obj = dict2MAB(m.to_dict())
    assert isinstance(obj, AB)
    assert obj.current_arm == 0


def test_dict2MAB_AnnealingSoftmax():
    m = AnnealingSoftmax([10, 20], [0.1, 0.5])

    obj = dict2MAB(m.to_dict())
    assert isinstance(obj, AnnealingSoftmax)

def test_dict2MAB_Softmax():
    m = Softmax(0.2, [10, 20], [0.1, 0.5])

    obj = dict2MAB(m.to_dict())
    assert isinstance(obj, Softmax)
    assert obj.temperature == 0.2


def test_dict2MAB_BetaTS():
    m = BetaTS([1, 2], [3, 4], [10, 20], [0.1, 0.5])

    obj = dict2MAB(m.to_dict())
    assert isinstance(obj, BetaTS)
    assert obj.alpha == [1, 2]
    assert obj.beta == [3, 4]


def test_dict2MAB_EpsilonGreedy():
    m = EpsilonGreedy(0.6, [10, 20], [0.1, 0.5])

    obj = dict2MAB(m.to_dict())
    assert isinstance(obj, EpsilonGreedy)
    assert obj.epsilon == 0.6


def test_dict2MAB_RandomSelect():
    m = RandomSelect([10, 20], [0.1, 0.5])

    obj = dict2MAB(m.to_dict())
    assert isinstance(obj, RandomSelect)

def test_dict2MAB_UCB1():
    m = UCB1([10, 20], [0.1, 0.5])

    obj = dict2MAB(m.to_dict())
    assert isinstance(obj, UCB1)
