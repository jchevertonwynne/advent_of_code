#!/usr/local/bin/python3

import time

input_filename = "../../input/input_day15.txt"


def generate_options(state, world, checked):
    x, y = state.coords
    history = state.history
    options = []
    for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
        if world[ny][nx] == '.' and (nx, ny) not in checked:
            checked.add((nx, ny))
            new_history = history[:] + [(nx, ny)]
            options.append(State((nx, ny), new_history))
    return options


def travel(start, end, game):
    world = game.world
    checked = set()
    options = generate_options(State(start, []), world, checked)
    while options:
        next_options = []
        for option in options:
            next_options.extend(generate_options(option, world, checked))
        options = []
        if next_options:
            acceptable = [next_option for next_option in next_options if next_option.history[-1] == end]
            if acceptable:
                sx, sy = start
                for pref_coords in [(sx, sy - 1), (sx - 1, sy), (sx + 1, sy), (sx, sy + 1)]:
                    for accept in acceptable:
                        if accept.history[0] == pref_coords:
                            return accept
            options = next_options


class State:
    def __init__(self, coords, history):
        self.coords = coords
        self.history = history

    def __repr__(self):
        return f"coords: {self.coords}, history: {self.history}"

    def copy(self):
        return State(self.coords, self.history[:], self.checked.copy())


class Fighter:
    def __init__(self, species, x, y, add_to):
        self.species = species
        self.x = x
        self.y = y
        self.hp = 200
        self.attack = 3
        add_to.append(self)

    def __repr__(self):
        return f"{self.species}(x: {self.x}, y: {self.y}, hp: {self.hp})"

    def __str__(self):
        return self.species


class Game:
    def __init__(self, world, fighters):
        self.world = world
        self.fighters = fighters
        self.turn = 0

    def step(self):
        self.turn += 1
        self.fighters.sort(key=lambda f: (f.y, f.x))

        surr = {f: [(nx, ny)
                    for nx, ny in [(f.x, f.y + 1), (f.x, f.y - 1), (f.x + 1, f.y), (f.x - 1, f.y)]
                    if self.world[ny][nx] == '.']
                for f in self.fighters}

        for fighter in self.fighters:
            f_x, f_y = fighter.x, fighter.y
            opps = [opp for opp in self.fighters if opp.species != fighter.species]
            if not opps:
                return "Done"
            print()
            print(repr(fighter))
            print('i have opps')
            next_to = [opp for opp in opps if abs(opp.x - fighter.x) + abs(opp.y - fighter.y) == 1]
            if next_to:
                if len(next_to) == 1:
                    Game.fight(self, fighter, next_to[0])
                else:
                    next_to.sort(key=lambda o: o.hp)
                    if next_to[0].hp < next_to[1].hp:
                        Game.fight(self, fighter, next_to[0])
                    else:
                        weakest = [opp for opp in next_to if opp.hp == next_to[0].hp]
                        
                        Game.fight(self, fighter, weakest)
            tile_options = []
            for opp in opps:
                tile_options.extend(surr[opp])
            distances = []
            for option in tile_options:
                nav = travel((fighter.x, fighter.y), option, self)
                if nav is not None:
                    distances.append((option, nav.history))
            if distances:
                best_coords, dist = min(distances, key=lambda d: len(d[1]))

                print(best_coords)
                print()

    def fight(self, attacker, victim):
        victim.hp -= attacker.attack
        if victim.hp <= 0:
            print('lol')

    def print_world(self):
        for row in self.world:
            print(''.join(char if isinstance(char, str) else str(char) for char in row))


def setup():
    with open(input_filename) as f:
        fighters = []
        world = [[Fighter(char, x, y, fighters) if char in 'GE' else char
                  for x, char in enumerate(row.strip())] for y, row in enumerate(f)]
        return Game(world, fighters)


def part1(game):
    game.step()
    return 0


def part2():
    return 0


def main():
    start_setup = time.time()
    game = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(game)
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

# if __name__ == '__main__':
#     main()

# print(travel((11, 3), (22, 18), setup()))

w = setup()
# w.world[27][24] = "!"
# w.world[14][1] = "?"
w.print_world()
