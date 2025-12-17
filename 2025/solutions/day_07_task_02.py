from functools import cache

from helpers import Puzzle


puzzle = Puzzle(day=7)


def main(lines: list[str]) -> int:
    n = len(lines[0])
    m = len(lines)

    @cache
    def recurse(x: int, y: int) -> int:
        if x < 0 or x >= n:
            return 0
        if y >= m:
            return 1
        
        if lines[y][x] == ".":
            return recurse(x, y+1)
        else:
            return recurse(x+1, y+1) + recurse(x-1, y+1)

    start_x = lines[0].find("S")
    return recurse(start_x, 1)


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))