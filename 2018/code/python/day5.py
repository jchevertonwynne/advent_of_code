#!/usr/local/bin/python3

from string import ascii_lowercase, ascii_uppercase
import time

input_filename = "../../input/input_day5.txt"


def reduce_polarities(polymer):
    out = []
    for char in polymer:
        if not out:
            out.append(char)
        elif char != out[-1] and char.upper() == out[-1].upper():
            out.pop()
        else:
            out.append(char)
    return "".join(out)


def setup():
    with open(input_filename) as f:
        return f.read().strip()


def part1(polymer):
    return reduce_polarities(polymer)


def part2(polymer):
    shortest = len(polymer)
    for a1, a2 in zip(ascii_lowercase, ascii_uppercase):
        modified_polymer = polymer.replace(a1, "").replace(a2, "")
        modified_shortened = reduce_polarities(modified_polymer)
        if len(modified_shortened) < shortest:
            shortest = len(modified_shortened)
    return shortest


def main():
    start_setup = time.time()
    polymer = setup()
    end_setup = time.time()

    start_part1 = time.time()
    reduced = part1(polymer)
    res_part1 = len(reduced)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(reduced)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")


if __name__ == "__main__":
    main()
