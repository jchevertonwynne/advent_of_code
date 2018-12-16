#!/usr/local/bin/python3

import time
from parse import parse
from collections import Counter

input_filename = "../../input/input_day4.txt"

def parse_dates():
    records = []
    with open(input_filename) as f:
        for row in f.read().splitlines():
            day, time, action = parse("[{} {}] {}", row)
            records.append((day, time, action))
    records.sort(key=lambda x: (x[0], x[1]))
    return records

def setup():
    guards = {}
    for date, time, action in parse_dates():
        if action.startswith('G'):
            guard, = parse("Guard #{:d} begins shift", action)
            if not guard in guards:
                guards[guard] = [Counter(), 0]
        elif action.startswith('f'):
            begin_time = parse("{:d}:{:d}", time)[1]
        elif action.startswith('w'):
            end_time = parse("{:d}:{:d}", time)[1]
            guards[guard][0].update(range(begin_time, end_time))
            guards[guard][1] += end_time - begin_time
    return guards

def part1(guards):
    id, (counter, total) = max(guards.items(), key=lambda x: x[1][1])
    min, freq = counter.most_common(1)[0]
    return id * min

def part2(guards):
    reduced = ((id, *count.most_common(1)[0]) for id, (count, total) in guards.items() if len(count) > 0)
    id, min, freq = max(reduced, key=lambda x: x[2])
    return id * min

def main():
    start_setup = time.time()
    guards = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(guards)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(guards)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
