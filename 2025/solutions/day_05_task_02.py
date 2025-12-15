from helpers import Puzzle
from ranges import Range, RangeSet


puzzle = Puzzle(day=5)


def main(f: str) -> int:
    ranges = f.split("\n\n")[0]
    ranges = RangeSet([Range(*map(int, line.split("-")), include_end=True) for line in ranges.splitlines()])
    count = 0

    for r in ranges:
        count += r.length() + 1

    return count

if __name__ == "__main__":
    print(main(puzzle.sample()))
    print(main(puzzle.raw_content))