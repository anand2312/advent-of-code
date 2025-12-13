from helpers import Puzzle


puzzle = Puzzle(day=4)


def main(lines: list[str]) -> int:
    count = 0
    for (y, line) in enumerate(lines):
        for (x, pt) in enumerate(line):
            if pt == ".":
                continue
            
            dots = 0
            for (n_y, n_x) in [
                (y-1, x-1), (y-1, x), (y-1, x+1),
                (y, x-1), (y, x+1),
                (y+1, x-1), (y+1, x), (y+1, x+1)
            ]:
                try:
                    if n_y < 0 or n_x < 0:
                        # negative indexing is fine in python, dummy.
                        raise IndexError
                    if lines[n_y][n_x] == ".":
                        dots += 1
                except IndexError:
                    dots += 1
            if dots > 4:
                count += 1
    return count
            


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))