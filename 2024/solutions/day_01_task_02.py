from collections import Counter
from helpers import Puzzle


puzzle = Puzzle(day=1)


def main(lines: list[str]) -> int:
    l1, l2 = [], []

    for line in lines:
        left, right = line.split()
        l1.append(int(left))
        l2.append(int(right))
    
    counter = Counter(l2)

    accum = 0

    for i in l1:
        accum += i * counter.get(i, 0)
    
    return accum


if __name__ == "__main__":
    sample = """3   4
4   3
2   5
1   3
3   9
3   3"""
    print(main(sample.splitlines()))
    print(main(puzzle.lines()))