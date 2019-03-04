#!/usr/local/bin/python3

from typing import List, Tuple, Dict
import time
from parse import parse
from collections import Counter

input_filename = "../../input/input_day4.txt"


class Guard:
    def __init__(self):
        self.sleep_counter = Counter()
        self.total_sleep = 0

Record = Tuple[str, str, str]
Records = List[Record]
GuardDict = Dict[int, Guard]

def parse_dates() -> Records:
    records = []
    with open(input_filename) as f:
        for row in f.read().splitlines():
            day, time, action = parse("[{} {}] {}", row)
            records.append((day, time, action))
    records.sort(key=lambda x: (x[0], x[1]))
    return records


def setup() -> GuardDict:
    guards: GuardDict = {}
    for _, time, action in parse_dates():
        if action.startswith("G"):
            guard, = parse("Guard #{:d} begins shift", action)
            if guard not in guards:
                guards[guard] = Guard()
        elif action.startswith("f"):
            begin_time = parse("{:d}:{:d}", time)[1]
        elif action.startswith("w"):
            end_time = parse("{:d}:{:d}", time)[1]
            guards[guard].sleep_counter.update(range(begin_time, end_time))
            guards[guard].total_sleep += end_time - begin_time
    return guards


def part1(guards: GuardDict) -> int:
    guard_id, guard = max(guards.items(), key=lambda g: g[1].total_sleep)
    least, _ = guard.sleep_counter.most_common(1)[0]
    return guard_id * least


def part2(guards: GuardDict) -> int:
    reduced = (
        (guard_id, guard.total_sleep, *guard.sleep_counter.most_common(1)[0])
        for guard_id, guard in guards.items()
        if len(guard.sleep_counter) > 0
    )
    guard_id, least, *_ = max(reduced, key=lambda x: x[1])
    return guard_id * least


def main() -> None:
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


if __name__ == "__main__":
    main()
