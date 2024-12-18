from helpers import Puzzle


puzzle = Puzzle(day=4)


def sides(y: int, x: int, n: int, m: int) -> list[list[tuple[int, int]]]:
    """Return indices to check horizontally, vertically and diagonally (and all of them in reverse)."""
    out = []

    forwards = []
    backwards = []
    upwards = []
    downwards = []
    diag_1 = []  # diagonal into 1st quadrant
    diag_2 = []
    diag_3 = []
    diag_4 = []

    if x >= 3:  # there are enough chars behind
        backwards = [(x-1, y), (x-2, y), (x-3, y)]
    if m - x > 3:
        forwards = [(x+1, y), (x+2, y), (x+3, y)]
    if y >= 3:
        upwards = [(x, y-1), (x, y-2), (x, y-3)]
    if n - y > 3:
        downwards = [(x, y+1), (x, y+2), (x, y+3)]
    if m - x > 3 and y >= 3:
        diag_1 = [(x+1, y-1), (x+2, y-2), (x+3, y-3)]
    if x >= 3 and y >= 3:
        diag_2 = [(x-1, y-1), (x-2, y-2), (x-3, y-3)]
    if x >= 3 and n - y > 3:
        diag_3 = [(x-1, y+1), (x-2, y+2), (x-3, y+3)]
    if m - x > 3 and n - y > 3:
        diag_4 = [(x+1, y+1), (x+2, y+2), (x+3, y+3)]
    
    out.extend([backwards, forwards, upwards, downwards, diag_1, diag_2, diag_3, diag_4])
    return out


def main(lines: list[str]) -> int:
    n, m = len(lines), len(lines[0])
    matches = 0

    for y in range(n):
        for x in range(m):
            if lines[y][x] == "X":
                possibilities = sides(y, x, n, m)
                for side in possibilities:
                    if not side: continue
                    for (x_i, y_i), to_match in zip(side, "MAS"):
                        if lines[y_i][x_i] != to_match:
                            break
                    else:

                        matches += 1
    
    return matches


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))