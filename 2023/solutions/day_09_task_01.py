from collections import defaultdict
from itertools import pairwise
from helpers import Puzzle

def extrapolate(line: list[int]) -> int:
    n = len(line)
    nums = defaultdict(int)
    for idx, val in enumerate(line):
        nums[(0, idx)] = val
    curr = line.copy()
    base_idx = 1
    y = 1
    while not (all(i == 0 for i in curr)):
        new_curr = []
        for idx, pair in enumerate(pairwise(curr)):
            nums[(y, base_idx + idx)] = pair[1] - pair[0]
            new_curr.append(pair[1] - pair[0])
        base_idx += 1
        y += 1
        curr = new_curr

    y -= 1  # last iteration of loop would've incremented it unnecessarily

    for i in range(y - 1, -1, -1):
        nums[(i, n)] = nums[(i, n - 1)] + nums[(i + 1, n)]  # left + down
    return nums[(0, n)]


def main(lines: list[str]) -> int:
    intlines = [[int(i) for i in line.split()] for line in lines]
    return sum(map(extrapolate, intlines))

if __name__ == "__main__":
    puzzle = Puzzle(day=9)
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))