import time

def part1():
    with open("input_day1.txt") as f:
        vals = (int(x) for x in f.readlines())
        return(sum(vals))

def part2():
    freqs = set((0,))
    freq = 0
    with open("input_day1.txt") as f:
        vals = list(int(x) for x in f.readlines())
        while True:
            for val in vals:
                freq += val
                if freq in freqs:
                    return freq
                else:
                    freqs.add(freq)
                # print(len(freqs))

start = time.time()
print(part1())
print(f"part 1 took {time.time() - start} seconds")
start = time.time()
print(part2())
print(f"part 2 took {time.time() - start} seconds")
