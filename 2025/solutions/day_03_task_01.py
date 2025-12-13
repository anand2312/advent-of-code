from helpers import Puzzle
from functools import cache


puzzle = Puzzle(day=3)


@cache
def recurse(bank: str, idx: int, batteries_on: int, batteries_needed: int) -> str:
    n = len(bank)

    if idx == n:
        return ''
    if batteries_on == batteries_needed:
        return ''
    
    # take - i.e turn the current battery on
    take = bank[idx] + recurse(
        bank,
        idx + 1,
        batteries_on + 1,
        batteries_needed
    )
    # skip - i.e don't turn the current battery on, go on to the next
    skip = recurse(
        bank,
        idx + 1,
        batteries_on,
        batteries_needed
    )
    return take if int(take) > int(skip if skip else 0) else skip


def main(lines: list[str]) -> int:
    return sum([int(recurse(line, 0, 0, 2)) for line in lines])


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))