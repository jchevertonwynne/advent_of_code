#!/usr/local/bin/python3

import time
from parse import parse

input_filename = "../../input/input_day10.txt"

class Point:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def iterate(self):
        self.x, self.y = self.x + self.dx, self.y + self.dy

def get_min_max(points, coord):
    if coord== 'x':
        min_x = min(points, key=lambda p: p.x).x
        max_x = max(points, key=lambda p: p.x).x
        return min_x, max_x
    else:
        min_y = min(points, key=lambda p: p.y).y
        max_y = max(points, key=lambda p: p.y).y
        return min_y, max_y

def setup():
    points = []
    with open(input_filename) as f:
        for line in f.read().splitlines():
            x, y, dx, dy = parse("position=<{:d},{:d}>velocity=<{:d},{:d}>", line.replace(" ", ""))
            points.append(Point(x, y, dx, dy))
    return points

def part1(points):
    iterations = 0
    min_y, max_y = get_min_max(points, 'y')
    while max_y  - min_y > 9:
        iterations += 1
        for point in points:
            point.iterate()
        min_y, max_y = get_min_max(points, 'y')
    min_x, max_x = get_min_max(points, 'x')
    x_width, y_width = max_x - min_x + 1, max_y - min_y + 1
    out = [["." for _ in range(x_width)] for _ in range(y_width)]
    for point in points:
        out[point.y - min_y][point.x - min_x] = "#"
    for row in out:
        print("".join(row))
    return iterations

def main():
    start_setup = time.time()
    points = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part2 = part1(points)
    end_part1 = time.time()

    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 & 2 took {end_part1 - start_part1} seconds")
    print(f"overall took {end_part1 - start_setup} seconds")

if __name__ == '__main__':
    main()
