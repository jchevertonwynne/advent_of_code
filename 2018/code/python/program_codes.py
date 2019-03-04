from parse import parse
import time


class Rule:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"{type(self).__name__} {self.a} {self.b} {self.c}"


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


class Computer:
    def __init__(self, ip, ins):
        self.ip = ip
        self.ins = ins
        self.state = [0, 0, 0, 0, 0, 0]
    
    def process(self, debug=False):
        if debug:
            instruction = self.state[self.ip]
            print()
            rule = self.ins[instruction]
            print(instruction, rule)
            print(self.state)
            rule.apply_rule(self.state)
            print(self.state)
            self.state[self.ip] += 1
            print(self.state)
            time.sleep(0.2)
        else:
            instruction = self.state[self.ip]
            self.ins[instruction].apply_rule(self.state)
            self.state[self.ip] += 1


def create_computer(input_filename):
    opcodes = {'addr': Addr, 'addi': Addi,
               'mulr': Mulr, 'muli': Muli,
               'banr': Banr, 'bani': Bani,
               'borr': Borr, 'bori': Bori,
               'setr': Setr, 'seti': Seti,
               'gtir': Gtir, 'gtri': Gtri, 'gtrr': Gtrr,
               'eqir': Eqir, 'eqri': Eqri, 'eqrr': Eqrr}
    with open(input_filename) as f:
        lines = iter(f.read().splitlines())
        opc, = parse('#ip {:d}', next(lines))
        ins_list = []
        for line in lines:
            ins, a, b, c = parse('{} {:d} {:d} {:d}', line)
            ins_list.append(opcodes[ins](a, b, c))
    return Computer(opc, ins_list)
