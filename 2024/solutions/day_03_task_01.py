from helpers import Puzzle
import re


puzzle = Puzzle(day=3)


def main(memory: str) -> int:
    pattern = "mul\((\d+,\d+)\)"
    accum = 0
    for m in re.finditer(pattern, memory):
        operands = m.group(1)
        x, y = [int(i) for i in operands.split(",")]
        accum += x * y
    return accum


if __name__ == "__main__":
    print(main(puzzle.sample()))
    print(main(puzzle.raw_content))