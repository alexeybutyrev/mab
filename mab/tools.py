from . import (
    AB,
    UCB1,
    Softmax,
    BetaTS,
    EpsilonGreedy,
    RandomSelect,
    AnnealingSoftmax,
)


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
