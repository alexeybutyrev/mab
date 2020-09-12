# __init__.py

__version__ = "0.1.1"

from mab.montecarlo import test_alorythm
from mab.rewards import BernoulliArm
from mab.rewards import UniformArm
from mab.epsilongreedy import EpsilonGreedy
from mab.randomselect import RandomSelect
from mab.annealingsoftmax import AnnealingSoftmax
from mab.metric import Metric
from mab.ab import AB
from mab.ucb1 import UCB1
from mab.softmax import Softmax