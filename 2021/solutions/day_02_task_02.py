from helpers import Puzzle
from day_02_task_01 import parse_line


puzzle = Puzzle(day=2)


def main() -> int:
    hor, ver, aim = 0, 0, 0
    instructions = map(parse_line, puzzle.lines())

    for mvmt, amt in instructions:
        if mvmt == "forward":
            hor += amt
            ver += aim * amt
        elif mvmt == "down":
            aim += amt
        else:
            aim -= amt
    
    return hor * ver


print(main())
