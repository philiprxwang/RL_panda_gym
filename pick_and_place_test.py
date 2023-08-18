import gymnasium as gym
import panda_gym
import time

env = gym.make("PandaPickAndPlace-v3", render_mode="human")
observation, info = env.reset()

images = [env.render()]
for _ in range(200):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    images.append(env.render())

    if terminated or truncated:
        observation, info = env.reset()
        images.append(env.render())

    time.sleep(0.1)

env.close()