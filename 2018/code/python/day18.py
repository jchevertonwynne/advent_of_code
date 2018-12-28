#!/usr/local/bin/python3

import time
from collections import Counter
from itertools import count

input_filename = "../../input/input_day18.txt"

def get_surrounding(x, y, world):
    x_lim = len(world[0])
    y_lim = len(world)
    res = Counter()

    if x >= 1:
        res[world[y][x - 1]] += 1
        if y >= 1:
            res[world[y - 1][x - 1]] += 1
        if y <= y_lim - 2:
            res[world[y + 1][x - 1]] += 1
    if x <= x_lim - 2:
        res[world[y][x + 1]] += 1
        if y >= 1:
            res[world[y - 1][x + 1]] += 1
        if y <= y_lim - 2:
            res[world[y + 1][x + 1]] += 1
    if y >= 1:
        res[world[y - 1][x]] += 1
    if y <= y_lim - 2:
        res[world[y + 1][x]] += 1

    return res

def calc_next(x, y, world):
    tile = world[y][x]
    surrounding = get_surrounding(x, y, world)
    if tile == '.':
        return '|' if surrounding['|'] >= 3 else '.'
    elif tile == '|':
        return '#' if surrounding['#'] >= 3 else '|'
    else:
        return '#' if surrounding['#'] >= 1 and surrounding['|'] >= 1 else '.'

def step_world(world):
    return [[calc_next(x, y, world) for x, char in enumerate(row)] for y, row in enumerate(world)]

def sim_world(world, n):
    for _ in range(n):
        world = step_world(world)
    tiles = Counter(char for row in world for char in row)
    return tiles['|'] * tiles['#']

def world_string(world):
    return ''.join(''.join(row) for row in world)

def auto_world(world):
    while True:
        world = step_world(world)
        yield world

def setup():
    with open(input_filename) as f:
        return [[char for char in row] for row in f.read().splitlines()]
    
def part1(world):
    return sim_world(world, 10)

def part2(world):
    seen = {world_string(world): 0}
    for i, world in zip(count(1), auto_world(world)):
        stringified = world_string(world)
        if stringified in seen:
            cycle = i - seen[stringified]
            remainder = (1_000_000_000 - i) % cycle
            return sim_world(world, remainder)
        else:
            seen[stringified] = i

def main():
    start_setup = time.time()
    world = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(world)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(world)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
