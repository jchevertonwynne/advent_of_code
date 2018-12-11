#!/usr/local/bin/python3

import time
import numpy as np

input_filename = "../../input/input_day1.txt"

def power(x, y, sn):
    id = x + 10
    level = id * y
    level += sn
    level *= id
    hnd = level // 100 % 10
    return hnd - 5

def setup(sn):
    return np.fromfunction(lambda x, y :power(x, y, sn), (300, 300))

def part1(grid):
    best = 0
    coords = 0, 0
    for x in range(298):
        for y in range(298):
            temp = np.sum(grid[x:x+3, y:y+3])
            if temp > best:
                best = temp
                coords = x, y
    return coords

def part2(grid):
    best = 0
    coords = 0, 0, 0
    for size in range(1, 301):
        if not size % 10:
            print(size)
        for x in range(300 - size):
            for y in range(300 - size):
                temp = np.sum(grid[x:x+size, y:y+size])
                if temp > best:
                    best = temp
                    coords = x + 1, y + 1, size
    return coords

def main():
    sn = 6042

    start_setup = time.time()
    grid = setup(sn)
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(grid)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(grid)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
