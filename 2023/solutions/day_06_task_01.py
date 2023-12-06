import re
from helpers import Puzzle


def main(lines: list[str]) -> int:
    times = [int(i) for i in re.findall(r"\d+", lines[0])]
    distances = [int(i) for i in re.findall(r"\d+", lines[1])]
    total = 1

    for time, distance in zip(times, distances):
        wins = 0
        for i in range(1, time + 1):
            if i * (time - i) > distance:
                wins += 1
        total *= wins
    return total


if __name__ == "__main__":
    puzzle = Puzzle(day=6)
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))
