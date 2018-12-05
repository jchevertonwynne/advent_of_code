#!/usr/local/bin/python3

import time
from itertools import cycle

input_filename = "input/input_day1.txt"

def get_vals():
    with open(input_filename) as f:
        vals = [int(x) for x in f.read().splitlines()]
        return vals

def part1(vals):
    return sum(vals)

def part2(vals):
    freqs = {0}
    freq = 0
    for val in cycle(vals):
        freq += val
        if freq in freqs:
            return freq
        else:
            freqs.add(freq)

start = time.time()
vals = get_vals()
print(f"setup took {time.time() - start} seconds")

start = time.time()
print(part1(vals))
print(f"part 1 took {time.time() - start} seconds")

start = time.time()
print(part2(vals))
print(f"part 2 took {time.time() - start} seconds")
