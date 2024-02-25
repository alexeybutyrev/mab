"""Names and Constants"""
from enum import Enum, auto


class AutoName(Enum):
    """"Define Enum Values"""

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.upper()


class Metrics(AutoName):
    """"Metrics Enum"""

    ACCURACY = auto()
    AVERAGE_REWARD = auto()
    CUMULATIVE_REWARD = auto()
    REGRET = auto()
    COMPARE_TO_AB = auto()


CORE_METRICS = [
    Metrics.ACCURACY,
    Metrics.AVERAGE_REWARD,
    Metrics.CUMULATIVE_REWARD,
    Metrics.REGRET,
]
