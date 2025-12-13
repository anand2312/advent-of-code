from helpers import Puzzle
from day_03_task_01 import recurse


puzzle = Puzzle(day=3)


def main(lines: list[str]) -> int:
    return sum([int(recurse(line, 0, 0, 12)) for line in lines])


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))