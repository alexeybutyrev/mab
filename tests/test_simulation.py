import pytest
import mab.ab as ab
import mab.epsilongreedy as eg
import mab.ucb as ucb1
import mab.betats as betats
import mab.rewards as rewards
import simpy
import mab.realtime as realtime


@pytest.fixture
def mu():
    return [0.6, 0.1, 0.1]


@pytest.fixture
def n_arms(mu):
    return len(mu)


@pytest.fixture
def horizon():
    return 120


@pytest.fixture
def n_customers_low():
    return 50


@pytest.fixture
def n_customers_high():
    return 100


@pytest.fixture
def algorithms(n_arms):
    return [
        ab.AB(n_arms=n_arms),
        eg.EpsilonGreedy(0.8, n_arms=n_arms),
        ucb1.UCB1(n_arms=n_arms),
        betats.BetaTS(n_arms=n_arms),
    ]


def test_fixtures(mu, n_arms, algorithms):
    assert len(mu) == n_arms
    assert sum(mu) == pytest.approx(0.8)
    assert type(algorithms) == list
    assert len(algorithms) == 4


@pytest.mark.smoke
def test_simulation(mu, n_arms, horizon, algorithms, n_customers_low, n_customers_high):
    metrics = []
    names = []

    for a in algorithms:
        arms = list(map(lambda x: rewards.BernoulliArm(x), mu))

        env = simpy.Environment()

        s = realtime.UISimulation(
            env,
            algorithm=a,
            arms=arms,
            n_customers_low=n_customers_low,
            n_customers_high=n_customers_high,
        )
        env.run(until=horizon)

        s.calculate_metrics()

        metrics.append(s.metrics)
        names.append(s.name)
    assert len(metrics) == len(algorithms)
    assert len(names) == len(algorithms)
