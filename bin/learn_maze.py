import gym
from gym import spaces
import numpy as np

class MazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    def __init__(self, maze):
        super(MazeEnv, self).__init__()
        self.maze = maze
        self.start_pos = tuple(np.argwhere(self.maze == 2)[0])
        self.end_pos = tuple(np.argwhere(self.maze == 3)[0])
        self.current_pos = self.start_pos
        
        self.action_space = spaces.Discrete(4)
        
        self.observation_space = spaces.Box(low=0, high=1, shape=self.maze.shape, dtype=np.int)
        
    def reset(self):
        self.current_pos = self.start_pos
        return self._get_obs()
    
    def step(self, action):
        new_pos = list(self.current_pos)
        
        if action == 0:
            new_pos[0] -= 1
        elif action == 1:
            new_pos[1] += 1
        elif action == 2:
            new_pos[0] += 1
        elif action == 3:
            new_pos[1] -= 1
        
        if self._is_valid_move(new_pos):
            self.current_pos = tuple(new_pos)
        
        done = self.current_pos == self.end_pos
        reward = 1 if done else -0.1
        
        return self._get_obs(), reward, done, {}
    
    def render(self, mode='human'):
        maze_copy = self.maze.copy()
        maze_copy[self.current_pos] = 'A'
        for row in maze_copy:
            print(' '.join(row))
        print()
    
    def close(self):
        pass
    
    def _get_obs(self):
        obs = np.zeros_like(self.maze, dtype=np.int)
        obs[self.current_pos] = 1
        return obs
    
    def _is_valid_move(self, pos):
        if (0 <= pos[0] < self.maze.shape[0] and
            0 <= pos[1] < self.maze.shape[1] and
            self.maze[pos[0], pos[1]] != '0'):
            return True
        return False