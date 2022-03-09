from gym.envs.registration import register

register(
	id='gym_sum-v0',
	entry_point='gym_sumo.envs:SumoEnv',
)