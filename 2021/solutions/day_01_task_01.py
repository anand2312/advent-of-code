from helpers import Puzzle


puzzle = Puzzle(day=1)


def main() -> int:
    count = 0
    depths = puzzle.intlines()

    for i, j in zip(depths, depths[1:]):
        if i < j:
            count += 1

    return count

print(main())