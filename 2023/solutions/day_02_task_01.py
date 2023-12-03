import re
from collections import defaultdict
from helpers import Puzzle


Turn = tuple[int, int, int]
Parsed = dict[int, list[Turn]]
r, g, b = 12, 13, 14


def parse_input(lines: list[str]) -> Parsed:
    out = defaultdict(list)
    pattern = re.compile(
        r"(?P<red>\d+)(?= red)|(?P<green>\d+)(?= green)|(?P<blue>\d+)(?= blue)"
    )
    for line in lines:
        group, rest = line.split(": ")
        group_id = int(group[4:])
        for turn in rest.split("; "):
            matches = list(pattern.finditer(turn))
            r, g, b = None, None, None
            for match in matches:
                if val := match.group("red"):
                    r = int(val)
                elif val := match.group("green"):
                    g = int(val)
                elif val := match.group("blue"):
                    b = int(val)
            out[group_id].append((r, g, b))
    return out


def check(tup: Turn) -> bool:
    turn_r, turn_g, turn_b = tup
    return bool(
        (turn_r and turn_r > r) or (turn_b and turn_b > b) or (turn_g and turn_g > g)
    )


def main(lines: list[str]) -> int:
    parsed = parse_input(lines)
    total = 0
    for key, value in parsed.items():
        if any([check(i) for i in value]):
            continue
        total += key
    return total


if __name__ == "__main__":
    sample = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    puzzle = Puzzle(day=2)
    print(main(sample.splitlines()))
    print(main(puzzle.lines()))
