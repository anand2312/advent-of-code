import numpy as np
from helpers import Puzzle


puzzle = Puzzle(day=9)


def parse_input(raw: str) -> np.ndarray:
    return np.array([list(map(int, line)) for line in raw.splitlines()])


def main(raw: str) -> int:
    lines = parse_input(raw)
    padded = np.pad(lines, 1, "constant", constant_values=9)

    # make another array that's padded at all sides with 9 (9 being the largest number wont affect comparisons)
    # then use this to compare each element with it's neighbours

    lows = (
        (lines < padded[2:, 1:-1])  # shift upwards
        & (lines < padded[:-2, 1:-1])  # downwards
        & (lines < padded[1:-1, 2:])  # right
        & (lines < padded[1:-1, :-2])  # left
    )

    return (lines[lows] + 1).sum()


if __name__ == "__main__":
    raw = puzzle.raw_content
    print(main(raw))
