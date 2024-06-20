import os
import sys
import argparse
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TOP_REPO_PATH = os.path.dirname(os.path.abspath(__file__))

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Description of your script")
    parser.add_argument('-x', type=int, help='size of maze horizontally', required=True)
    parser.add_argument('-y', type=int, help='size of the maze veritically', required=True)
    return parser.parse_args()

def generate_maze(x: int, y: int) -> list:

    maze = np.ones((y,x), dtype=int)

    start_x, start_y = (random.randint(0, (x - 3) // 2) * 2 + 1, random.randint(0, (y - 3) // 2) * 2 + 1)
    maze[start_y, start_x] = 0

    walls = [(start_x, start_y, start_x + 2, start_y), (start_x, start_y, start_x, start_y + 2)]

    def in_bounds(x_pos, y_pos):
        return 0 <= x_pos < x and 0 <= y_pos < y
    
    
    
def main():
    args = parse_args()

    x = args.x
    y = args.y

    maze = generate_maze(x,y)

if __name__ == '__main__':
    main()