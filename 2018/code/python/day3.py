#!/usr/local/bin/python3

import numpy as np
import time
from parse import parse

input_filename = "../../input/input_day3.txt"


def setup():
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


def main():
    start_setup = time.time()
    grid, vals = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(grid)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(grid, vals)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")


if __name__ == '__main__':
    main()
