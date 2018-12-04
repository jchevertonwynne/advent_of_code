#!/usr/local/bin/python3

from collections import Counter
import time

input_filename = "input/input_day2.txt"

def part1():
    def has_num(totals, num):
        for i, v in totals:
            if v == num:
                return True
        return False

    twos_count = 0
    threes_count = 0

    with open(input_filename) as f:
        for id in f.readlines():
            totals = Counter(id).most_common()
            if has_num(totals, 2):
                twos_count += 1
            if has_num(totals, 3):
                threes_count += 1

    return twos_count * threes_count


def part2():
    with open(input_filename) as f:
        ids = f.readlines()
        for ind, id1 in enumerate(ids):
            for id2 in ids[ind + 1:]:
                common = "".join(x for x, y in zip(id1, id2) if x == y)
                if len(common) == len(id1) - 1:
                    return common

start = time.time()
print(part1())
print(f"part 1 took {time.time() - start} seconds")
start = time.time()
print(part2())
print(f"part 2 took {time.time() - start} seconds")
