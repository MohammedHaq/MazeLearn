import os
import sys
import argparse
import gym
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import generate_maze as gm
import learn_maze as lm

TOP_REPO_PATH = os.path.dirname(os.path.abspath(__file__))

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Description of your script")
    parser.add_argument('-x', type=int, help='Width of the maze', required=True)
    parser.add_argument('-y', type=int, help='height of the maze', required=True)
    return parser.parse_args()

def main():

    args = parse_args()
    x = args.x
    y = args.y 

    maze = gm.generate_maze(x,y)
    for row in maze:
        print(' '.join(['#' if cell == 1 else ' ' if cell == 0 else 'S' if cell == 2 else 'E' for cell in row]))

    env = lm.MazeEnv(maze)

    gym.envs.registration.register(
    id='CustomMaze-v0',
    entry_point=lm.MazeEnv,
    max_episode_steps=100,
    )

    
    


    
if __name__ == '__main__':
    main()