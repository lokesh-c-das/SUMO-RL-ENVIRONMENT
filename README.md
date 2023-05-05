# SUMO-RL-ENVIRONMENT
An example of how to create a custom openAI gym like Environment for Simulation of Urban MObility SUMO and reinforcement learning agant

# Installation
- Install [SUMO](https://sumo.dlr.de/docs/Downloads.php)
- Install custom gym for SUMO
```ruby
git clone git@github.com:lokesh-c-das/SUMO-RL-ENVIRONMENT.git
cd gym_sumo
pip install -e .
```

# Example
##### The following example shows how to use custom SUMO gym environment for your reinforcement learning algorithms.
```python
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
	env.closeEnvConnection() # close SUMO Environment Connection
if __name__ == '__main__':
	test()
```
