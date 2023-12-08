import math
from helpers import Puzzle
from day_08_task_01 import parse, solve


def main(lines: list[str]) -> int:
    instructions, adj_list = parse(lines)
    steps = [solve(instructions, adj_list, start) for start in adj_list if start.endswith("A")]
    return math.lcm(*steps)


if __name__ == "__main__":
    puzzle = Puzzle(day=8)
    print(main(puzzle.lines()))
