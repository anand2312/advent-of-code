from day_02_task_01 import parse_input
from helpers import Puzzle


def key_none_as_zero(a: int | None) -> int:
    # in the parsed inputs, every tuple has 3 elements regardless of whether
    # a turn had all three colours. if a colour did not exist in a turn,
    # it has None as it's value instead of 0
    # this function changes the None to a 0 for comparison
    return a if a else 0


def main(lines: list[str]) -> int:
    parsed = parse_input(lines)
    power = 0
    for key, value in parsed.items():
        reds, greens, blues = zip(*value)
        min_reds = max(reds, key=key_none_as_zero)
        min_greens = max(greens, key=key_none_as_zero)
        min_blues = max(blues, key=key_none_as_zero)
        power += min_reds * min_blues * min_greens
    return power


if __name__ == "__main__":
    sample = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    puzzle = Puzzle(day=2)
    print(main(sample.splitlines()))
    print(main(puzzle.lines()))
