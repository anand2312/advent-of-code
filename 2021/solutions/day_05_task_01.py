from collections import Counter
from typing import List, Optional, Set, Tuple

from helpers import Puzzle


puzzle = Puzzle(day=5)


def parse_input(raw: str) -> List[List[List[int]]]:
    out = []
    for line in raw.splitlines():
        start, end = line.split(" -> ")
        start = [int(i) for i in start.split(",")]
        end = [int(i) for i in end.split(",")]
        out.append([start, end])
    return out


def get_straight_lines(lines: List[List[List[int]]]) -> List[List[List[int]]]:
    """Filter out only the lines which are horizontal or vertical"""
    out = []

    for line in lines:
        start, end = line
        x1, y1 = start
        x2, y2 = end

        if x1 == x2 or y1 == y2:
            out.append(line)
    
    return out


def get_points(line: List[List[int]]) -> Optional[Set[Tuple[int, int]]]:
    """Get the set of points a given (horizontal or vertical) line passes through."""
    start, end = line
    x1, y1 = start
    x2, y2 = end

    if x1 == x2:
        if y1 > y2:
            big = y1
            small = y2
        else:
            big = y2
            small = y1
        return {(x1, i) for i in range(small, big + 1)}
    elif y1 == y2:
        if x1 > x2:
            big = x1
            small = x2
        else:
            big = x2
            small = x1
        return {(i, y1) for i in range(small, big + 1)}

def main() -> int:
    """Determine the points at which at least two lines intersect."""
    raw_input = puzzle.raw_content
    all_lines = parse_input(raw_input)
    counter = Counter()

    for line in get_straight_lines(all_lines):
        points = get_points(line)
        counter.update(points)
    
    greater_than_2 = list(filter(lambda i: i[1] >= 2, counter.most_common()))
    return len(greater_than_2)

if __name__ == "__main__":
    print(main())
