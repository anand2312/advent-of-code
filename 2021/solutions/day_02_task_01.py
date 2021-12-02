from typing import Tuple
from helpers import Puzzle


puzzle = Puzzle(day=2)


def parse_line(ln: str) -> Tuple[str, int]:
    # parses an instruction line into a 2-tuple
    # where the first element is the instruction
    # and the second element is the amount
    l = ln.split()
    return l[0], int(l[1])


def main() -> int:
    hor, ver = 0, 0
    instructions = map(parse_line, puzzle.lines())

    for mvmt, amt in instructions:
        if mvmt == "forward":
            hor += amt
        elif mvmt == "down":
            ver += amt
        else:
            ver -= amt
    
    return hor * ver
