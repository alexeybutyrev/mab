from mab.ab import AB
from mab.ucb1 import UCB1
from mab.annealingsoftmax import AnnealingSoftmax
from mab.betats import BetaTS
from mab.softmax import Softmax
from mab.epsilongreedy import EpsilonGreedy
from mab.randomselect import RandomSelect


def dict2MAB(d: dict):
    """ Returns object of MAB from the dictionary

    Args:
        d (dict): dictionary with the class attributes like name and internal paramters
    """
    class_mapping = {
        "AB": AB,
        "UCB1": UCB1,
        "Softmax": Softmax,
        "BetaTS": BetaTS,
        "EpsilonGreedy": EpsilonGreedy,
        "RandomSelect": RandomSelect,
        "AnnealingSoftmax": AnnealingSoftmax,
    }

    class_instance = class_mapping[d["name"]]
    parameters = d["params"]
    object = class_instance(**parameters)
    return object
