#!/usr/local/bin/python3

from string import ascii_lowercase, ascii_uppercase
import time
from functools import reduce

input_filename = "input/input_day5.txt"

def reduce_polarities(polymer):
    last = polymer
    while True:
        polymer = reduce(lambda a, b: a if a[-1] != b and a[-1].upper() == b.upper() else a + b, polymer)
        if polymer == last:
            return polymer
        last = polymer

def get_contents():
    with open(input_filename) as f:
        contents = f.read().strip()
        return contents

def part1(polymer):
    return len(reduce_polarities(polymer))

def part2(polymer):
    shortest = len(polymer)
    for a1, a2 in zip(ascii_lowercase, ascii_uppercase):
        # modified_polymer = reduce(lambda a, b: a if b in (a1, a2) else a + b, polymer)
        modified_polymer = polymer.replace(a1, '').replace(a2, '')
        modified_shortened = reduce_polarities(modified_polymer)
        if len(modified_shortened) < shortest:
            shortest = len(modified_shortened)
    return shortest



start = time.time()
polymer = get_contents()
print(f"setup took {time.time() - start} seconds")
start = time.time()
print(part1(polymer))
print(f"part 1 took {time.time() - start} seconds")
start = time.time()
print(part2(polymer))
print(f"part 2 took {time.time() - start} seconds")
