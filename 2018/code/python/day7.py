#!/usr/local/bin/python3

import time
from parse import parse
from string import ascii_uppercase
from collections import defaultdict

input_filename = "../../input/input_day7.txt"

class Step:
    def __init__(self, letter, time):
        self.letter = letter
        self.time = time

def get_next_options(done, reqs):
    options = []
    for letter in ascii_uppercase:
        if letter not in done:
            prior = reqs[letter]
            if prior <= set(done):
                options.append(letter)
    return options

def available_option(done, active, reqs):
    options = get_next_options(done, reqs)
    active = [l.letter for l in active]
    for option in options:
        if option not in done and option not in active:
            prior = reqs[option]
            if prior <= set(done):
                return option

def fill_active(done, active, reqs):
    option = available_option(done, active, reqs)
    while len(active) < 5 and option:
        active.append(Step(option, ord(option) - 4))
        option = available_option(done, active, reqs)
    return active

def process_active(done, active):
    new_active = []
    for letter in active:
        letter.time -= 1
        if letter.time == 0:
            done.append(letter.letter)
        else:
            new_active.append(letter)
    return done, new_active

def setup():
    letters = defaultdict(set)
    with open(input_filename) as f:
        for ordering in f.read().splitlines():
            prior, next = parse('Step {} must be finished before step {} can begin.', ordering)
            letters[next].add(prior)
    return letters

def part1(reqs):
    done = []
    options = get_next_options(done, reqs)
    while options:
        done.append(options[0])
        options = get_next_options(done, reqs)
    return "".join(done)

def part2(reqs):
    time = -1
    active = []
    done = []
    while len(done) < 26:
        done, active = process_active(done, active)
        active = fill_active(done, active, reqs)
        time += 1
    return time

def main():
    start_setup = time.time()
    reqs = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(reqs)
    end_part1 = time.time()

    start_part2= time.time()
    res_part2 = part2(reqs)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
