#!/usr/local/bin/python3

from collections import Counter
import time

input_filename = "../../input/input_day2.txt"

def has_num(totals, num):
    for i, v in totals:
        if v == num:
            return True
    return False

def check_sim(str1, str2):
    diff = 0
    for a, b in zip(str1, str2):
        if a != b:
            diff += 1
            if diff == 2:
                return False
    return True

def setup():
    with open(input_filename) as f:
        return f.read().splitlines()

def part1(ids):
    twos_count = 0
    threes_count = 0

    for id in ids:
        totals = Counter(id).most_common()
        if has_num(totals, 2):
            twos_count += 1
        if has_num(totals, 3):
            threes_count += 1

    return twos_count * threes_count

def part2(ids):
    for ind, id1 in enumerate(ids):
        for id2 in ids[ind + 1:]:
            if check_sim(id1, id2):
                return "".join(x for x, y in zip(id1, id2) if x == y)

def main():
    start_setup = time.time()
    vals = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(vals)
    end_part1 = time.time()

    start_part2= time.time()
    res_part2 = part2(vals)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
