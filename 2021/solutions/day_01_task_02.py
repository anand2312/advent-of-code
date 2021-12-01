from helpers import Puzzle


puzzle = Puzzle(day=1)


def main() -> int:
    depths = puzzle.intlines()
    count = 0

    for i in range(len(depths) - 2):
        if i == 0:
            continue

        start, end = i, i + 3
        if end >= len(depths):
            break

        if depths[start] < depths[end]:
            count += 1

    return count

print(main())
