import math
from collections import Counter
from typing import List, Set, Tuple

from day_05_task_01 import parse_input, get_points as get_straight_line_points
from helpers import Puzzle


puzzle = Puzzle(day=5)

# a list containing two lists, where each inner list is x, y
LineType = List[List[int]]
PointType = Tuple[int, int]


def get_valid_lines(lines: List[LineType]) -> Tuple[List[LineType], List[LineType]]:
    hor_ver = []
    diagonal = []
    for line in lines:
        start, end = line
        x1, y1 = start
        x2, y2 = end

        # check for horizontal/vertical like before
        if x1 == x2 or y1 == y2:
            hor_ver.append(line)
        # check for diagonal line with slope 45
        # tan 45 = 1; 45 in the other side -> -1
        elif (x1 - x2) / (y1 - y2) in {1.0, -1.0}:
            diagonal.append(line)
    return hor_ver, diagonal


def get_diagonal_line_points(line: LineType) -> Set[PointType]:
    start, end = line
    x1, y1 = start
    x2, y2 = end

    sign = lambda a: (a > 0) - (a < 0)
    sign_x, sign_y = sign(x2 - x1), sign(y2 - y1)
    return set(zip(range(x1, x2 + sign_x, sign_x), range(y1, y2 + sign_y, sign_y)))


def main() -> int:
    raw_input = puzzle.raw_content
    all_lines = parse_input(raw_input)
    counter = Counter()

    straight_lines, diagonal_lines = get_valid_lines(all_lines)

    for line in straight_lines:
        points = get_straight_line_points(line)
        counter.update(points)
    
    for line in diagonal_lines:
        points = get_diagonal_line_points(line)
        counter.update(points)
    
    greater_than_2 = list(filter(lambda i: i[1] >= 2, counter.most_common()))
    return len(greater_than_2)

if __name__ == "__main__":
    print(main())
