#!/usr/local/bin/python3

import time

input_filename = "../input/input_day8.txt"

class Node:
    def __init__(self, ind, child_remainging, data_len):
        self.ind = ind
        self.child_remaining = child_remainging
        self.data_len = data_len
        self.children = []
        self.data_vals = []

    def __repr__(self):
        return f"Node(ind: {self.ind}, metadata items:{self.data_len}, children:{len(self.children)})"

def setup():
    with open(input_filename) as f:
        return [int(i) for i in f.read().split(' ')]

def part1(nums):
    stack = []
    total = 0
    ind = 0
    base = Node(0, nums[0], nums[1])
    stack.append(base)
    while stack:
        top = stack[-1]
        if top.child_remaining == 0:
            stack.pop()
            top.data_vals = nums[(ind + 2):(ind + top.data_len + 2)]
            total += sum(top.data_vals)
            ind += top.data_len
        else:
            ind += 2
            next = Node(ind, nums[ind], nums[ind + 1])
            stack.append(next)
            top.child_remaining -= 1
            top.children.append(next)
    return base, total

def part2(node):
    if not node.children:
        return sum(node.data_vals)
    return sum(part2(node.children[data_val - 1]) for data_val in node.data_vals if data_val < len(node.children) + 1)

def main():
    start_setup = time.time()
    nums = setup()
    end_setup = time.time()

    start_part1 = time.time()
    base, res_part1 = part1(nums)
    end_part1 = time.time()

    start_part2= time.time()
    res_part2 = part2(base)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")

if __name__ == '__main__':
    main()
