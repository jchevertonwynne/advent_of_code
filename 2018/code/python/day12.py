#!/usr/local/bin/python3

import time
from parse import parse
from collections import defaultdict

input_filename = "../../input/input_day12.txt"

class Plants:
    def __init__(self, plants, rules):
        self.plants = plants
        self.rules = rules
        self.min_ind = min(filter(lambda i: plants[i] == "#", plants))
        self.max_ind = max(filter(lambda i: plants[i] == "#", plants))

    def generation(self):
        new_plants = {}
        for ind in range(self.min_ind - 2, self.max_ind + 3):
            bin_rep = "".join(self.plants.get(i, ".") for i in range(ind - 2, ind + 3))\
                       .replace("#", "1").replace(".", "0")
            new_plants[ind] = self.rules.get(int(bin_rep, 2), ".")
        self.plants = new_plants
        self.min_ind = min(filter(lambda i: self.plants[i] == "#", self.plants))
        self.max_ind = max(filter(lambda i: self.plants[i] == "#", self.plants))

    def display(self):
        return str(self.min_ind) + "".join(self.plants.get(i, ".") for i in range(self.min_ind, self.max_ind))

def setup():
    rules = {}
    plants = {}
    with open(input_filename) as f:
        init = next(f)
        board = parse("initial state: {}", init)[0]
        plants = {i:v for i, v in enumerate(board)}
        next(f)
        for rule in f:
            state, outcome = parse("{} => {}", rule)
            state = int(state.replace("#", "1").replace(".", "0"), 2)
            rules[state] = outcome
    return Plants(plants, rules)

def part1(plants):
    for _ in range(20):
        plants.generation()
    return sum(filter(lambda p: plants.plants[p] == "#", plants.plants))

def part2(plants):
    for i in range(50_000_000_000):
        if not i % 10000:
            tot = sum(filter(lambda p: plants.plants[p] == "#", plants.plants))
            print(f"{i}: {tot}")
        plants.generation()
    return sum(filter(lambda p: plants.plants[p] == "#", plants.plants))

def main():
    start_setup = time.time()
    plants1 = setup()
    plants2 = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(plants1)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(plants2)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
