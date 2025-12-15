from operator import mul, add
from typing import Literal
from helpers import Puzzle


puzzle = Puzzle(day=6)


def main(lines: list[str]) -> int:
    worksheet = [line.split() for line in lines]
    op_column: list[Literal["*", "+"]] = worksheet[-1]  # type: ignore
    op_map = {
        "*": mul,
        "+": add
    }

    results: list[int] = []

    for line in worksheet[:-1]:
        if len(results) == 0:
            results = [int(i) for i in line]
            continue
        for (idx, i) in enumerate(line):
            results[idx] = op_map[op_column[idx]](results[idx], int(i))

    return sum(results)


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))