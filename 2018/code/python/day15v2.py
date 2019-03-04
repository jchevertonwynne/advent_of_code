from typing import List, Tuple

input_filename = "../../input/input_day15.txt"


class Fighter:
    def __init__(self, pos, fighters):
        self.pos = pos
        fighters.append(self)

    def __str__(self):
        return str(self.pos)


class Game:
    def __init__(self, world, fighters):
        self.world = world
        self.fighters = fighters
        self.turn = 0


def setup():
    with open(input_filename) as f:
        fighters = []
        world = [[Fighter(char, (x, y), fighters) if char in 'GE' else char
                  for x, char in enumerate(row.strip())] for y, row in enumerate(f)]
        return Game(world, fighters)


def generate_options(history, world, checked):
    x, y = history[-1] # get current coord
    options = []
    for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]: # adjacent options
        if world[ny][nx] == '.' and (nx, ny) not in checked: # walkable terrain and not visited
            checked.add((nx, ny)) # mark as seen
            new_history = history[:] + [(nx, ny)] # create new list and add new coord onto
            options.append(new_history) # add to list of visitable options
    return options


def travel(start: Tuple[int, int], end: Tuple[int, int], world: List[List[str]]):
    checked = set()
    options = generate_options([start], world, checked)
    while options: # if there are ways to go
        next_options = []
        for option in options:
            next_options.extend(generate_options(option, world, checked)) # for each way, find where they can go
        options = []
        if next_options: # if i can move further
            acceptable = [next_option for next_option in next_options if next_option.history[-1] == end]
            if acceptable: # if i have reached my goal
                return acceptable # reutrn all successful paths
            options = next_options


world_map = setup().world