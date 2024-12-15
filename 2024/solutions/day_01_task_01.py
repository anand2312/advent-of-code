from helpers import Puzzle


puzzle = Puzzle(day=1)


def main(lines: list[str]) -> int:
    l1, l2 = [], []

    for line in lines:
        left, right = line.split()
        l1.append(int(left))
        l2.append(int(right))
    
    l1.sort()
    l2.sort()

    accum = 0

    for x, y in zip(l1, l2):
        accum += abs(x - y)
    
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
