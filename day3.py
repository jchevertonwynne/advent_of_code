import numpy as np
import time
import parse

def generate_usage_grid_and_vals():
    grid = np.zeros((1000, 1000))
    vals = []
    with open("input_day3.txt") as f:
        for row in f.readlines():
            id, x_start, y_start, x_size, y_size = map(int, parse.parse("#{} @ {},{}: {}x{}", row))
            grid[x_start:x_start + x_size, y_start:y_start + y_size] += 1
            vals.append((id, x_start, y_start, x_size, y_size))
    return grid, vals


def part1():
    grid, _ = generate_usage_grid_and_vals()
    return (grid >= 2).sum()

def part2():
    grid, vals = generate_usage_grid_and_vals()
    for id, x_start, y_start, x_size, y_size in vals:
        if (grid[x_start:x_start + x_size, y_start:y_start + y_size] == 1).all():
            return id
    return None

start = time.time()
print(part1())
print(f"part 1 took {time.time() - start} seconds")
start = time.time()
print(part2())
print(f"part 2 took {time.time() - start} seconds")
