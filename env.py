import gym
from gym import spaces

class Env(gym.Env):
    metadata = {'render.modes': ['rgb_array']}

    def __init__(self, env_config=None):
        super(Env, self).__init__()
        self.action_space = spaces.Discrete(2)