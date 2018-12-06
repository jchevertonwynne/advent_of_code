#!/usr/local/bin/python3

import time
from parse import parse
from collections import defaultdict
from functools import reduce

input_filename = "../input/input_day6.txt"

def setup():
    coords = set()
    with open(input_filename) as f:
        for coord in f.read().splitlines():
            x, y = parse('{:d}, {:d}', coord)
            coords.add((x, y))
    return coords

def part1(coords):
    infinite = set()
    best_counts = defaultdict(int)

    for j in range(-150, 551):
        for i in range(-150, 551):
            best_dist = 10**10
            best_coord = None
            for coord in coords:
                x, y = coord
                dist = abs(x - i) + abs(y - j)
                if dist < best_dist:
                    best_dist = dist
                    best_coord = coord
                elif dist == best_dist:
                    best_coord = None
            if best_coord is not None:
                best_counts[best_coord] += 1
            if i in (-150, 550) or j in (-150, 550):
                infinite.add(best_coord)

    most_pop = sorted(best_counts.items(), key=lambda c: c[1])
    for coord, freq in reversed(most_pop):
        if coord not in infinite:
            return best_counts[coord]

def part2(coords):
    total = 0
    board = [[(x, y) for y in range(-150, 551)] for x in range(-150, 551)]
    for col in board:
        for (x, y) in col:
            dist = sum(abs(x - i) + abs( y - j) for i, j in coords)
            if dist < 10000:
                total += 1
    return total

def main():
    start_setup = time.time()
    coords = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(coords)
    end_part1 = time.time()

    start_part2= time.time()
    res_part2 = part2(coords)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
