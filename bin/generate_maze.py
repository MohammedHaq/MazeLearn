import random
import numpy as np

def generate_maze(x: int, y: int) -> list:

    maze = np.ones((y,x), dtype=int)

    start_x, start_y = (random.randint(0, (x - 3) // 2) * 2 + 1, random.randint(0, (y - 3) // 2) * 2 + 1)
    maze[start_y, start_x] = 0

    walls = [(start_x, start_y, start_x + 2, start_y), (start_x, start_y, start_x, start_y + 2)]

    def in_bounds(x_pos, y_pos):
        return 0 <= x_pos < x and 0 <= y_pos < y
    
    while walls:
        x1, y1, x2, y2 = random.choice(walls)
        walls.remove((x1, y1, x2, y2))
        
        if in_bounds(x2, y2) and maze[y2, x2] == 1:
            maze[y2, x2] = 0
            maze[(y1 + y2) // 2, (x1 + x2) // 2] = 0
            
            for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
                nx, ny = x2 + dx, y2 + dy
                if in_bounds(nx, ny) and maze[ny, nx] == 1:
                    walls.append((x2, y2, nx, ny))

    maze[0, :] = 1  
    maze[-1, :] = 1  
    maze[:, 0] = 1  
    maze[:, -1] = 1  

    def is_not_border(x_pos, y_pos):
        return 1 < x_pos < x - 1 and 1 < y_pos < y - 1

    exit_x, exit_y = start_x, start_y
    while not is_not_border(exit_x, exit_y) or (exit_x == start_x and exit_y == start_y):
        exit_x, exit_y = (random.randint(1, (x - 3) // 2) * 2 + 1, random.randint(1, (y - 3) // 2) * 2 + 1)

    maze[start_y, start_x] = 2  # Mark the start point
    maze[exit_y, exit_x] = 3    # Mark the end point

    return maze