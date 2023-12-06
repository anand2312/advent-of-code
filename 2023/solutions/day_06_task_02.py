import re
from helpers import Puzzle


def main(lines: list[str]) -> int:
    time = int("".join(re.findall(r"\d+", lines[0])))
    distance = int("".join(re.findall(r"\d+", lines[1])))
    i = 0
    # hmm, observing the sample - we just need to find when
    # we start beating the distance as we start increasing speed from 1...
    # the maximum value that still beats the distance is time - i
    # so the total number of winning ways = (time - i) - i + 1 = time - 2i + 1
    while i * (time - i) < distance:
        i += 1
    return (time - 2 * i) + 1


if __name__ == "__main__":
    puzzle = Puzzle(day=6)
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))
