#!/usr/local/bin/python3

import numpy as np
import time
from parse import parse

input_filename = "input/input_day3.txt"

def generate_usage_grid_and_vals():
    grid = np.zeros((1000, 1000))
    vals = []
    with open(input_filename) as f:
        for row in f.read().splitlines():
            id, x_start, y_start, x_size, y_size = parse("#{:d} @ {:d},{:d}: {:d}x{:d}", row)
            grid[x_start:x_start + x_size, y_start:y_start + y_size] += 1
            vals.append((id, x_start, y_start, x_size, y_size))
    return grid, vals

def part1(grid):
    return (grid >= 2).sum()

def part2(grid, vals):
    for id, x_start, y_start, x_size, y_size in vals:
        if (grid[x_start:x_start + x_size, y_start:y_start + y_size] == 1).all():
            return id
    return None

start = time.time()
grid, vals = generate_usage_grid_and_vals()
print(f"setup took {time.time() - start} seconds")

start = time.time()
print(part1(grid))
print(f"part 1 took {time.time() - start} seconds")

start = time.time()
print(part2(grid, vals))
print(f"part 2 took {time.time() - start} seconds")
