from helpers import Puzzle


puzzle = Puzzle(day=1)


def main() -> int:
    depths = puzzle.intlines()
    count = 0
    sums = list(map(sum, chunked(depths)))

    for i, _sum in enumerate(sums):
        if i == 0:
            continue
        if _sum > sums[i-1]:
            count += 1

    return count


def chunked(it: list, size: int = 3):
    for i in range(len(it)):
        chunk = it[i: i + size]

        if len(chunk) != size:
            break
        else:
            yield chunk

print(main())
