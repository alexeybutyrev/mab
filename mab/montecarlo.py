from copy import deepcopy


def mc_simulation(algs, arms, num_sims, horizon):
    """Monte Carlo simulation of MAB algorythms

    Args:
        algs (list): List of MAB alogorythms
        arms (RewardClass): List with arms giving the rewards
        num_sims (int): Number of simulations
        horizon (int): Time horizon (max t)

    Returns:
        [dict]: keys: algorytms names
                values: simulation, times, chosesen arms, rewards, cummulative rewards
    """
    chosen_arms = [0.0 for i in range(num_sims * horizon)]
    rewards = [0.0 for i in range(num_sims * horizon)]
    cumulative_rewards = [0.0 for i in range(num_sims * horizon)]
    sim_nums = [0.0 for i in range(num_sims * horizon)]
    times = [0.0 for i in range(num_sims * horizon)]
    possible_rewards = [0.0 for i in range(num_sims * horizon)]

    alg_output = {
        "sim_nums": sim_nums,
        "times": times,
        "chosen_arms": chosen_arms,
        "rewards": rewards,
        "cumulative_rewards": cumulative_rewards,
        "possible_rewards": possible_rewards,
    }
    result = {}
    for a in algs:
        result[a.name] = deepcopy(alg_output)
        result[a.name]["marketing_name"] = a.marketing_name

    for sim in range(num_sims):

        for a in algs:
            a.reset()

        for t in range(horizon):
            for a in algs:
                index = sim * horizon + t
                result[a.name]["sim_nums"][index] = sim
                result[a.name]["times"][index] = t

                chosen_arm = a.select_arm()
                result[a.name]["chosen_arms"][index] = chosen_arm

                # check out if any rewards for the current time and simulation
                # save 0 in possible rewards and 1 otherwise
                all_rewards = list(map(lambda x: x.draw(), arms))
                result[a.name]["possible_rewards"][index] = int(sum(all_rewards) > 0)

                reward = all_rewards[chosen_arm]
                result[a.name]["rewards"][index] = reward

                if t == 0:
                    result[a.name]["cumulative_rewards"][index] = reward
                else:
                    result[a.name]["cumulative_rewards"][index] = (
                        result[a.name]["cumulative_rewards"][index - 1] + reward
                    )

                a.update(chosen_arm, reward)

    return result