#!/usr/local/bin/python3

import time
from operator import itemgetter

input_filename = "../../input/input_day20.txt"


def setup():
    frame = get_frame()
    world = {(0, 0): '@',
             (1, 0): '?',
             (-1, 0): '?',
             (0, 1): '?',
             (0, -1): '?',
             (1, 1): '#',
             (-1, -1): '#',
             (1, -1): '#',
             (-1, 1): '#'}
    x, y = 0, 0
    dir_list(world, frame, x, y)
    return world


def get_frame():
    frame = [[]]
    frames = [frame]
    with open(input_filename) as f:
        for char in f.read().strip()[1:-1]:
            if char in 'NESW':
                frames[-1][-1].append(char)
            elif char == '(':
                n = [[]]
                frames[-1][-1].append(n)
                frames.append(n)
            elif char == '|':
                frames[-1].append([])
            elif char == ')':
                frames.pop()
    return frame


def build_walls(world, x, y):
    world[(x, y)] = '.'

    if (x, y + 1) not in world:
        world[(x, y + 1)] = '?'
    if (x, y - 1) not in world:
        world[(x, y - 1)] = '?'
    if (x + 1, y) not in world:
        world[(x + 1, y)] = '?'
    if (x - 1, y) not in world:
        world[(x - 1, y)] = '?'
    return world


def navigate(world, chars, x, y):
    for tile in chars:
        if isinstance(tile, str):
            if tile in 'NESW':
                if tile == 'N':
                    world[(x, y + 1)] = '-'
                    y += 2
                elif tile == 'S':
                    world[(x, y - 1)] = '-'
                    y -= 2
                elif tile == 'E':
                    world[(x + 1, y)] = '|'
                    x += 2
                elif tile == 'W':
                    world[(x - 1, y)] = '|'
                    x -= 2
                build_walls(world, x, y)
        else:
            dir_list(world, tile, x, y)


def dir_list(world, chars, x, y):
    for directions in chars:
        navigate(world, directions, x, y)


def construct_map(world):
    min_x = min(world, key=itemgetter(0))[0]
    min_y = min(world, key=itemgetter(1))[1]
    max_x = max(world, key=itemgetter(0))[0]
    max_y = max(world, key=itemgetter(1))[1]
    return reversed([''.join([world.get((x, y), ' ') 
                     for x in range(min_x, max_x + 1)])
                     for y in range(min_y, max_y + 1)])


def get_next(world, coords, checked):
    x, y = coords
    options = []
    for xm, ym in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        wall_check = x + xm, y + ym
        new_tile = (x + 2 * xm, y + 2 * ym)
        if new_tile not in checked and world[wall_check] in '|-':
            checked.add(new_tile)
            options.append(new_tile)
    return options


def traverse_world(world):
    coords = 0, 0
    checked = {coords}
    options = get_next(world, coords, checked)
    iterations = 0
    dist_record = 0

    while options:
        iterations += 1
        next_options = []
        for option in options:
            next_options.extend(get_next(world, option, checked))
        if next_options:
            options = next_options
            if iterations >= 999:
                dist_record += len(next_options)
        else:
            return iterations, dist_record


def main():
    start_setup = time.time()
    world = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1, res_part2 = traverse_world(world)
    end_part1 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 and 2 took {end_part1 - start_part1} seconds")
    print(f"overall took {end_part1 - start_setup} seconds")


if __name__ == '__main__':
    main()
