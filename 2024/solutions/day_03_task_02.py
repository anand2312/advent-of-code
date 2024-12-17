from helpers import Puzzle
import re


puzzle = Puzzle(day=3)


def main(memory: str) -> int:
    pattern = "mul\((\d+,\d+)\)|do\(\)|don't\(\)"
    enabled = True
    accum = 0

    for m in re.finditer(pattern, memory):
        matched_str = m.group(0)
        if matched_str == "don't()":
            enabled = False
        elif matched_str == "do()":
            enabled = True
        else:
            if not enabled:
                continue
            operands = m.group(1)
            x, y = [int(i) for i in operands.split(",")]
            accum += x * y

    return accum


if __name__ == "__main__":
    print(main(puzzle.sample()))
    print(main(puzzle.raw_content))