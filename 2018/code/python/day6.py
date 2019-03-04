#!/usr/local/bin/python3

import time
from parse import parse
from collections import defaultdict
from functools import reduce

input_filename = "../../input/input_day6.txt"


def boundary_test(x, y, on_bound_only=False):
    if on_bound_only:
        op = int.__eq__
    else:
        op = int.__ge__
    if x > 200:
        if y > 200:
            return op(700, x + y)
        return op(300, x - y)
    if y > 200:
        return op(300, y - x)
    return op(x + y, 100)


def find_lims(col, coords):
    top = find_in_lim(col, coords)
    if top is None:
        return None, None
    else:
        return top, find_in_lim(reversed(col), coords)


def find_in_lim(col, coords):
    for (x, y) in col:
        dist = sum(abs(x - i) + abs(y - j) for i, j in coords)
        if dist <= 10_000:
            return y
    return None


def find_next_top(top, col, coords):
    x, y = col[top]
    dist = sum(abs(x - i) + abs(y - j) for i, j in coords)
    if dist > 10_000:
        while dist > 10_000:
            top += 1
            if top == len(col) + 1:
                return None
            x, y = col[top]
            dist = sum(abs(x - i) + abs(y - j) for i, j in coords)
        return top - 1
    while dist < 10_000:
        top -= 1
        if top == -1:
            return None
        x, y = col[top]
        dist = sum(abs(x - i) + abs(y - j) for i, j in coords)
    return top + 1


def find_next_bot(bot, col, coords):
    x, y = col[bot]
    dist = sum(abs(x - i) + abs(y - j) for i, j in coords)
    if dist > 10_000:
        while dist > 10_000:
            bot -= 1
            if bot == -1:
                return None
            x, y = col[bot]
            dist = sum(abs(x - i) + abs(y - j) for i, j in coords)
        return bot + 1
    while dist < 10_000:
        bot += 1
        if bot == len(col) + 1:
            return None
        x, y = col[bot]
        dist = sum(abs(x - i) + abs(y - j) for i, j in coords)
    return bot - 1


def setup():
    coords = set()
    with open(input_filename) as f:
        for coord in f.read().splitlines():
            x, y = parse("{:d}, {:d}", coord)
            coords.add((x, y))
    return coords


def part1(coords):
    infinite = set()
    best_counts = defaultdict(int)

    for j in range(-150, 551):
        for i in range(-150, 551):
            if boundary_test(i, j):
                best_dist = 10_000
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
                if boundary_test(i, j, True):
                    infinite.add(best_coord)

    most_pop = sorted(best_counts.items(), key=lambda c: c[1])
    for coord, freq in reversed(most_pop):
        if coord not in infinite:
            return best_counts[coord]


def part2(coords):
    total = 0
    board = [[(x, y) for y in range(-150, 551)] for x in range(-150, 551)]
    for col in board:
        top, bottom = find_lims(col, coords)
        if (top, bottom) != (None, None):
            total += bottom - top + 1
    return total


def main():
    start_setup = time.time()
    coords = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(coords)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(coords)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")


if __name__ == "__main__":
    main()
