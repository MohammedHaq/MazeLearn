import gym
from gym import spaces
import numpy as np

class MazeEnv(gym.Env):
    def __init__(self, maze):
        super(MazeEnv, self).__init__()
        self.maze = maze
        self.height, self.width = maze.shape
        self.start_pos = np.argwhere(maze == 2)[0]
        self.goal_pos = np.argwhere(maze == 3)[0]
        self.state = tuple(self.start_pos)

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=1, shape=(self.height, self.width), dtype=np.int)

    def reset(self):
        self.state = tuple(self.start_pos)
        return self.state

    def step(self, action):
        x, y = self.state

        if action == 0:    #up
            x -= 1
        elif action == 1:  #down
            x += 1
        elif action == 2:  #left
            y -= 1
        elif action == 3:  #right
            y += 1

        if self.maze[x, y] != 1:
            self.state = (x, y)

        done = self.state == tuple(self.goal_pos)
        reward = 1 if done else -0.1

        return self.state, reward, done, {}

    def render(self, mode='human'):
        maze_copy = np.copy(self.maze)
        x, y = self.state
        maze_copy[x, y] = 4