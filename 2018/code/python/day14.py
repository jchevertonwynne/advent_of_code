#!/usr/local/bin/python3

import time


def part1():
    recipes = [3, 7, 1, 0, 1, 0, 1]
    elf_a, elf_b = 6, 4
    while len(recipes) < 598711:
        points = recipes[elf_a] + recipes[elf_b]
        if points >= 10:
            recipes.extend(divmod(points, 10))
        else:
            recipes.append(points)

        recs = len(recipes)
        elf_a += recipes[elf_a] + 1
        elf_a %= recs
        elf_b += recipes[elf_b] + 1
        elf_b %= recs
    return "".join(str(r) for r in recipes[598701:598711])


def part2():
    wanted = [5, 9, 8, 7, 0, 1]
    recipes = [3, 7, 1, 0, 1, 0, 1]
    elf_a, elf_b = 6, 4
    while True:
        points = recipes[elf_a] + recipes[elf_b]
        if points >= 10:
            recipes.extend(divmod(points, 10))
        else:
            recipes.append(points)

        recs = len(recipes)
        elf_a += recipes[elf_a] + 1
        elf_a %= recs
        elf_b += recipes[elf_b] + 1
        elf_b %= recs

        if points >= 10 and recipes[-7:-1] == wanted:
            return len(recipes) - 7
        elif recipes[-6:] == wanted:
            return len(recipes) - 6


def main():
    start_part1 = time.time()
    res_part1 = part1()
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2()
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_part1} seconds")


if __name__ == '__main__':
    main()
