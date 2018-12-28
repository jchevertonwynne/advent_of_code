#!/usr/local/bin/python3

from typing import List
import time
from itertools import cycle

input_filename = "../../input/input_day1.txt"


def setup() -> List[int]:
    with open(input_filename) as f:
        return [int(x) for x in f.read().splitlines()]


def part1(vals: List[int]) -> int:
    return sum(vals)


def part2(vals: List[int]) -> int:
    freqs = {0}
    freq = 0
    for val in cycle(vals):
        freq += val
        if freq in freqs:
            return freq
        else:
            freqs.add(freq)


def main() -> None:
    start_setup = time.time()
    vals = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(vals)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(vals)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")


if __name__ == "__main__":
    main()
