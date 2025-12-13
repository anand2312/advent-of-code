from collections import defaultdict

from helpers import Puzzle

puzzle = Puzzle(day=4)


type Point = tuple[int, int]


def main(lines: list[str]) -> int:
    adjacent_rolls: dict[Point, set[Point]] = defaultdict(set)
    for (y, line) in enumerate(lines):
        for (x, spot) in enumerate(line):
            if spot == ".":
                continue

            for (n_y, n_x) in [
                (y-1, x-1), (y-1, x), (y-1, x+1),
                (y, x-1), (y, x+1),
                (y+1, x-1), (y+1, x), (y+1, x+1)
            ]:
                if n_y < 0 or n_x < 0 or n_y >= len(lines) or n_x >= len(lines[0]):
                    continue
                if (n_y, n_x) not in adjacent_rolls[(y, x)] and lines[n_y][n_x] == "@":
                    adjacent_rolls[(y, x)].add((n_y, n_x))
    
    old_count, new_count = 0, -1
    while old_count != new_count:
        old_count = new_count
        to_be_removed = []
        for (k, v) in adjacent_rolls.items():
            if len(v) < 4:
                to_be_removed.append(k)
                if new_count == -1:
                    new_count = 1
                else: 
                    new_count += 1
                for other_v in adjacent_rolls.values():
                    other_v.discard(k)
        for k in to_be_removed:
            adjacent_rolls.pop(k)
        
    return new_count


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))