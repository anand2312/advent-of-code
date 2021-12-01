from helpers import Puzzle


puzzle = Puzzle(day=1)


def main() -> int:
    count = 0
    depths = puzzle.intlines()

    for i, depth in enumerate(depths):
        if i == 0:
            continue
        if depth > depths[i - 1]:
            count += 1

    return count

print(main())