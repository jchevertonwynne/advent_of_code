#!/usr/local/bin/python3

import time
from parse import parse

input_filename = "../../input/input_day17.txt"

def setup():
    world = {}
    world[(0, 500)] = '+'
    with open(input_filename) as f:
        for line in f.read().splitlines():
            if line.startswith('x'):
                x, y1, y2 = parse('x={:d}, y={:d}..{:d}', line)
                for y in range(y1, y2 + 1):
                    world[(x, y)] = "#"
            else:
                y, x1, x2 = parse('y={:d}, x={:d}..{:d}', line)
                for x in range(x1, x2 + 1):
                    world[(x, y)] = "#"
    return world



def part1(world):
    max_y = max(world, key=lambda xy: xy[1])[1]
    active = [(500, 0)]
    while active and max(active, key=lambda xy: xy[1])[1] < max_y:
        x, y = active[-1]
        below = world.get((x, y + 1), None)
        if below is None:
            world[(x, y + 1)] = '|'
            active.append((x, y + 1))
        elif below in '#~':
            left = world.get((x - 1, y), '')
            right = world.get((x + 1, y), '')
            if any(side in '#~' for side in (left, right)):
                world[(x, y)] = '~'
                active.pop()
            for mx in [-1, 1]:
                if world.get((x + mx, y), None) is None:
                    world[(x + mx, y)] = '|'
                    active.append((x + mx, y))
        else:
            active.pop()
    return len([i for i, v in world.items() if v in '|~'])

def part2():
    return 0

def main():
    start_setup = time.time()
    world = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(world)
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
