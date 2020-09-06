def test_alorythm(algo, arms, num_sims, horizon):
    chosen_arms = [0.0 for i in range(num_sims*horizon)]
    rewards = [0.0 for i in range(num_sims*horizon)]
    cumulative_rewards = [0.0 for i in range(num_sims*horizon)]
    sim_nums = [0.0 for i in range(num_sims*horizon)]
    times = [0.0 for i in range(num_sims*horizon)]

    for sim in range(num_sims):
        algo.reset()
        for t in range(horizon):
            index = sim * horizon + t
            sim_nums[index] = sim
            times[index] = t

            chosen_arm = algo.select_arm()
            chosen_arms[index] = chosen_arm

            reward = arms[chosen_arm].draw()
            rewards[index] = reward
            if t == 0:
                cumulative_rewards[index] = reward
            else:
                cumulative_rewards[index] = cumulative_rewards[index-1] + reward

            algo.update(chosen_arm, reward)

    return {'sim_nums': sim_nums,
            'times': times,
            'chosen_arms': chosen_arms,
            'rewards': rewards,
            'cumulative_rewards': cumulative_rewards}
