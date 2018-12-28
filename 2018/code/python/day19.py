#!/usr/local/bin/python3

import time
from program_codes import Addr, Addi, Mulr, Muli, Banr, Bani, Borr, Bori, Setr, Seti, Gtir, Gtri, Gtrr, Eqir, Eqri, Eqrr, create_computer

input_filename = "../../input/input_day19.txt"

def setup():
    return create_computer(input_filename)

def part1(computer):
    while computer.state[computer.ip] < len(computer.ins):
        computer.process()
    return computer.state[0]

def part2(computer):
    last_ins = -1
    computer.state[0] = 1
    while last_ins < computer.state[computer.ip]:
        last_ins = computer.state[computer.ip]
        computer.process()
    biggest = computer.state[2]
    return sum(x for x in range(1, biggest + 1) if not biggest % x)

def main():
    start_setup = time.time()
    computer = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(computer)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(setup())
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
