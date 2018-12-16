#!/usr/local/bin/python3

import time
from parse import parse

input_filename = "../../input/input_day16.txt"

class InsChange:
    def __init__(self, before, ins, result):
        self.before = before
        self.ins = ins
        self.result = result

class Rule:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"{type(self)}, {self.a}, {self.b}, {self.c}"

class Addr(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        b = state[self.b]
        state[self.c] = a + b
        return state

class Addi(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        state[self.c] = a + self.b
        return state

class Mulr(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        b = state[self.b]
        state[self.c] = a * b
        return state

class Muli(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        state[self.c] = a * self.b
        return state

class Banr(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        b = state[self.b]
        state[self.c] = a & b
        return state

class Bani(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        state[self.c] = a & self.b
        return state

class Borr(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        b = state[self.b]
        state[self.c] = a | b
        return state

class Bori(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        state[self.c] = a | self.b
        return state

class Setr(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        state[self.c] = a
        return state

class Seti(Rule):
    def apply_rule(self, state):
        state[self.c] = self.a
        return state

class Gtir(Rule):
    def apply_rule(self, state):
        b = state[self.b]
        if self.a > b:
            state[self.c] = 1
        else:
            state[self.c] = 0
        return state

class Gtri(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        if a > self.b:
            state[self.c] = 1
        else:
            state[self.c] = 0
        return state

class Gtrr(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        b = state[self.b]
        if a > b:
            state[self.c] = 1
        else:
            state[self.c] = 0
        return state

class Eqir(Rule):
    def apply_rule(self, state):
        b = state[self.b]
        if self.a == b:
            state[self.c] = 1
        else:
            state[self.c] = 0
        return state

class Eqri(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        if a == self.b:
            state[self.c] = 1
        else:
            state[self.c] = 0
        return state

class Eqrr(Rule):
    def apply_rule(self, state):
        a = state[self.a]
        b = state[self.b]
        if a == b:
            state[self.c] = 1
        else:
            state[self.c] = 0
        return state

def apply_rule(applying, part1=True):
    ins_list = [Addr, Addi, Mulr, Muli, Banr, Bani, Borr, Bori,
                Setr, Seti, Gtir, Gtri, Gtrr, Eqir, Eqri, Eqrr]
    applied = [(ins, ins(*applying.ins[1:]).apply_rule(applying.before[:])) for ins in ins_list]
    if part1:
        return len([res for ins, res in applied if res == applying.result])
    else:
        return [ins for ins, res in applied if res == applying.result]

def setup():
    with open(input_filename) as f:
        lines = f.read().splitlines()
        prev_space = False
        part1_ins = []
        part2_ins = []
        lines = iter(lines)
        while True:
            line = next(lines)
            if line == '':
                if prev_space:
                    next(lines)
                    for line in lines:
                        part2_ins.append(tuple(parse('{:d} {:d} {:d} {:d}', line)))
                    return part1_ins, part2_ins
                prev_space = True
            else:
                prev_space = False
                before = list(parse("Before: [{:d}, {:d}, {:d}, {:d}]", line))
                ins = tuple(parse("{:d} {:d} {:d} {:d}", next(lines)))
                after = list(parse("After:  [{:d}, {:d}, {:d}, {:d}]", next(lines)))
                part1_ins.append(InsChange(before, ins, after))
        return part1, part2

def part1(ins_list):
    total = 0
    for ins in ins_list:
        if apply_rule(ins) >= 3:
            total += 1
    return total

def part2(ins_list, actual_data):
    opcodes = {}
    for ins in ins_list:
        res = apply_rule(ins, False)
        if ins.ins[0] in opcodes:
            opcodes[ins.ins[0]] = opcodes[ins.ins[0]] & set(res)
        else:
            opcodes[ins.ins[0]] = set(res)

    actual = {}
    while len(actual) < 16:
        for k, v in opcodes.items():
            if len(v) == 1:
                ins = v.pop()
                actual[k] = ins
                for code in opcodes:
                    if ins in opcodes[code]:
                        opcodes[code].remove(ins)

    opcodes = actual
    state = [0, 0, 0, 0]
    for ins in actual_data:
        apply = opcodes[ins[0]](*ins[1:])
        apply.apply_rule(state)
    return state[0]

def main():
    start_setup = time.time()
    ins1, ins2 = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(ins1)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(ins1, ins2)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
