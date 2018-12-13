#!/usr/local/bin/python3

import time
from collections import Counter, defaultdict

input_filename = "../../input/input_day13.txt"

class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.turn = 0
        self.crashed = False

    def __repr__(self):
        return f"Cart({self.x}, {self.y}, {self.direction}, {self.turn})"

class System:
    def __init__(self, carts, tracks):
        self.carts = carts
        self.tracks = tracks
        self.turns = 0
        self.max_x = max(self.tracks, key=lambda xy: xy[0])[0]
        self.max_y = max(self.tracks, key=lambda xy: xy[1])[1]

    def print_board(self):
        tracks = [[self.tracks.get((x, y), ' ') for x in range(self.max_x + 1)] for y in range(self.max_y + 1)]
        for cart in self.carts:
            x, y = cart.x, cart.y
            tracks[y][x] = cart.direction
        for row in tracks:
            print("".join(row))

    def process(self, first=True):
        self.turns += 1
        self.carts.sort(key=lambda c: c.x)
        self.carts.sort(key=lambda c: c.y)
        coords = defaultdict(list)
        coords.update({(cart.x, cart.y):[cart] for cart in self.carts})

        for cart in self.carts:
            if not cart.crashed:
                x, y = cart.x, cart.y
                if len(coords[(x, y)]) > 1:
                    for crashed in coords[(x, y)]:
                        crashed.crashed = True
                    if first:
                        return x, y
                else:
                    coords[(x, y)].remove(cart)

                    if cart.direction == '^':
                        y -= 1
                    elif cart.direction == 'v':
                        y += 1
                    elif cart.direction == '>':
                        x += 1
                    else:
                        x -= 1

                    cart.x, cart.y = x, y
                    coords[(x, y)].append(cart)

                    if first and len(coords[(x, y)]) > 1:
                        for crashed in coords[(x, y)]:
                            crashed.crashed = True
                        if first:
                            return x, y

                    tile = self.tracks[(x, y)]
                    if tile == "/":
                        if cart.direction == '^':
                            cart.direction = '>'
                        elif cart.direction == 'v':
                            cart.direction = '<'
                        elif cart.direction == '>':
                            cart.direction = '^'
                        else:
                            cart.direction = 'v'
                    if tile == "\\":
                        if cart.direction == '^':
                            cart.direction = '<'
                        elif cart.direction == 'v':
                            cart.direction = '>'
                        elif cart.direction == '>':
                            cart.direction = 'v'
                        else:
                            cart.direction = '^'
                    if tile == "+":
                        if cart.direction == '^':
                            cart.direction = ['<', '^', '>'][cart.turn % 3]
                        elif cart.direction == 'v':
                            cart.direction = ['>', 'v', '<'][cart.turn % 3]
                        elif cart.direction == '>':
                            cart.direction = ['^', '>', 'v'][cart.turn % 3]
                        else:
                            cart.direction = ['v', '<', '^'][cart.turn % 3]
                        cart.turn += 1

        self.carts = [cart for cart in self.carts if len(coords[(cart.x, cart.y)]) == 1]
        return None


def setup():
    cart_to_rail = {'>': '-',
                    '<': '-',
                    'v': '|',
                    '^': '|'}
    carts = []
    world = {}
    with open(input_filename) as f:
        for y, row in enumerate(f):
            for x, tile in enumerate(row.rstrip()):
                if tile != ' ':
                    if tile in "<>^v":
                        carts.append(Cart(x, y, tile))
                        world[(x, y)] = cart_to_rail[tile]
                    else:
                        world[(x, y)] = tile
    return System(carts, world)

def part1(system):
    run = system.process()
    while run is None:
        run = system.process()
        # system.print_board()
    print(system.turns)
    return run

def part2(system):
    while len(system.carts) > 1:
    # for _ in range(10):
        system.process(False)
        # system.print_board()
    print(system.turns)
    if len(system.carts) > 0:
        cart = system.carts[0]
        return cart.x, cart.y
    return 0

def main():
    start_setup = time.time()
    system1 = setup()
    system2 = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(system1)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(system2)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
