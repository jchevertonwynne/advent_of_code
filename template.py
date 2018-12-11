#!/usr/local/bin/python3

import time

input_filename = "../../input/input_day1.txt"

def setup():
    with open(input_filename) as f:
        return 0

def part1():
    return 0

def part2():
    return 0

def main():
    start_setup = time.time()
    vals = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1()
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2()
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
