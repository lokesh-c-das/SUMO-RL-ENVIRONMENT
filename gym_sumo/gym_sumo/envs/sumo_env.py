import os
import gym
import sys
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'],'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")
import traci
import sumolib


class SumoEnv(gym.Env):
	def __init__(self):
		print('Initialization done...')
	def start(self):
		print('Environment started...')
	def step(self):
		pass
	def action(self):
		pass
	def reset(self):
		pass
