#!/usr/local/bin/python3

import time
import parse
from collections import Counter

input_filename = "input/input_day4.txt"

def parse_dates():
    records = []
    with open(input_filename) as f:
        for row in f.readlines():
            day, time, action = parse.parse("[{} {}] {}", row)
            records.append((day, time, action))
    records.sort(key=lambda x: x[1])
    records.sort(key=lambda x: x[0])
    return records

def compile_frequencies(records):
    guards = {}
    for date, time, action in records:
        if action.startswith('G'):
            guard, = parse.parse("Guard #{:d} begins shift", action)
            if not guard in guards:
                guards[guard] = [Counter(), 0]
        elif action.startswith('f'):
            begin_time = parse.parse("{:d}:{:d}", time)[1]
        elif action.startswith('w'):
            end_time = parse.parse("{:d}:{:d}", time)[1]
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

start = time.time()
records = parse_dates()
guards = compile_frequencies(records)
print(f"setup took {time.time() - start} seconds")
start = time.time()
print(part1(guards))
print(f"part 1 took {time.time() - start} seconds")
start = time.time()
print(part2(guards))
print(f"part 2 took {time.time() - start} seconds")
