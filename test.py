import gym 
import gym_sumo
import numpy as np
import random
def test():
	# intialize sumo environment. If you do not need any gui,  render_mode=""
	env = gym.make("sumo-v0", render_mode="human") 
	env.reset()
	while True:
		action = random.randint(0,5) # your action
		observation, reward, done, _ = env.step(action)
		print(observation)
		if done:
			print('GoodBye!... Episode Ends')
			break
	env.closeEnvConnection() # end env connection





if __name__ == '__main__':
	test()
