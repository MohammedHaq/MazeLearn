import numpy as np
import random
import matplotlib.pyplot as plt

class QLearningAgent:
    def __init__(self, env, learning_rate=0.1, discount_factor=0.99, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.1):
        self.env = env
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.q_table = np.zeros((env.observation_space.shape[0], env.observation_space.shape[1], env.action_space.n))
        self.paths = []
    
    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return self.env.action_space.sample()
        else:
            return np.argmax(self.q_table[state[0], state[1]])
    
    def learn(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state[0], next_state[1]])
        td_target = reward + self.discount_factor * self.q_table[next_state[0], next_state[1], best_next_action]
        td_error = td_target - self.q_table[state[0], state[1], action]
        self.q_table[state[0], state[1], action] += self.learning_rate * td_error
    
    def train(self, episodes=1000):
        rewards = []
        for episode in range(episodes):
            state = self.env.reset()
            state = tuple(np.argwhere(state == 1)[0])
            total_reward = 0
            done = False
            
            while not done:
                action = self.choose_action(state)
                next_state, reward, done, _ = self.env.step(action)
                next_state = tuple(np.argwhere(next_state == 1)[0])
                
                self.learn(state, action, reward, next_state)
                
                state = next_state
                total_reward += reward
            
            rewards.append(total_reward)
            self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        
        return rewards
    
    def save_paths(self, filename):
        with open(filename, 'w') as f:
            for path in self.paths:
                for state in path:
                    f.write(f"{state[0]},{state[1]} ")
                f.write("\n")