import gymnasium as gym
import panda_gym
from stable_baselines3 import DDPG

env = gym.make('PandaReach-v3', render_mode="human")
model = DDPG(policy="MultiInputPolicy", env=env)
model.learn(30_000)