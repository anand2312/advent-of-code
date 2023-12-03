import itertools
import string
from helpers import Puzzle


Point = tuple[int, int]
NumberBounds = tuple[int, tuple[int, int]]


def nums_positions(lines: list[str]) -> tuple[dict[NumberBounds, int], int]:
    nums: dict[NumberBounds, int] = {}
    total = 0
    for y, line in enumerate(lines):
        for k, grp in itertools.groupby(enumerate(line), key=lambda i: i[1].isdigit()):
            if k:
                grp = list(grp)
                num_bounds = y, (grp[0][0], grp[-1][0])
                num = int("".join([i[1] for i in grp]))
                nums[num_bounds] = num
                total += num
    return nums, total


def is_neighbour(pt: Point, num: NumberBounds) -> bool:
    pt_x, pt_y = pt
    num_y, (num_start, num_end) = num
    if abs(pt_y - num_y) > 1:
        # more than one line apart
        return False
    if not (num_start - 1 <= pt_x <= num_end + 1):
        return False
    return True


def group_neighbours(num: NumberBounds) -> list[Point]:
    y, (start, end) = num
    return [
        *zip(
            range(start - 1, end + 2), itertools.repeat(y - 1)
        ),  # row above this number, accounting for diagonals
        *[(start - 1, y), (end + 1, y)],  # left and right on same row
        *zip(
            range(start - 1, end + 2), itertools.repeat(y + 1)
        ),  # row below this number
    ]


def main(lines: list[str]) -> int:
    y_up, x_up = len(lines), len(lines[0])
    num_positions, _ = nums_positions(lines)
    total = 0

    for bounds, num in num_positions.items():
        for x, y in group_neighbours(bounds):
            if not (0 <= x < x_up and 0 <= y < y_up):
                continue
            if lines[y][x] != "." and lines[y][x] in string.punctuation:
                total += num
                break

    return total


if __name__ == "__main__":
    puzzle = Puzzle(day=3)
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))
