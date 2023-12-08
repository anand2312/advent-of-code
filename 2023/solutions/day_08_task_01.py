from itertools import cycle
import re
from helpers import Puzzle


def parse(lines: list[str]) -> tuple[str, dict[str, tuple[str, str]]]:
    instructions = lines[0].strip()
    out = {}
    for line in lines[2:]:  # lines[1] is blank
        parent, left, right = re.findall(r"[1-9A-Z]{3}", line)
        out[parent] = (left, right)
    return instructions, out


def solve(instructions: str, adj_list: dict[str, tuple[str, str]], start: str) -> int:
    curr = start
    for idx, dir in enumerate(cycle(instructions)):
        curr = adj_list[curr][dir == "R"]
        if curr.endswith("Z"):
            return idx + 1
    return -1  # shut up, pyright


def main(lines: list[str]) -> int:
    instructions, adj_list = parse(lines)
    return solve(instructions, adj_list, "AAA")


if __name__ == "__main__":
    puzzle = Puzzle(day=8)
    # print(main(puzzle.sample_lines())) -- the sample input changed in p2
    print(main(puzzle.lines()))
