#!/usr/local/bin/python3

import time
from parse import parse
from itertools import cycle
from collections import deque

input_filename = "../input/input_day9.txt"

def setup():
    with open(input_filename) as f:
        for line in f.read().splitlines():
            players, last = parse("{:d} players; last marble is worth {:d} points", line)
    return players, last

def play_game(players, last):
    board = deque([0])
    scores = {i:0 for i in range(players)}
    for player, marble in zip(cycle(range(players)), range(1, last + 1)):
        if marble % 23:
            board.rotate(-2)
            board.appendleft(marble)
        else:
            board.rotate(7)
            val = board.popleft()
            scores[player] += marble
            scores[player] += val
    return max(scores.items(), key=lambda s: s[1])[1]

def part1(players, last):
    return play_game(players, last)

def part2(players, last):
    return play_game(players, last * 100)

def main():
    start_setup = time.time()
    players, last = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(players, last)
    end_part1 = time.time()

    start_part2= time.time()
    res_part2 = part2(players, last)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
