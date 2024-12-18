from helpers import Puzzle


puzzle = Puzzle(day=4)


def main(lines: list[str]) -> int:
    n, m = len(lines), len(lines[0])
    count = 0

    for y in range(n):
        for x in range(m):
            if lines[y][x] == "A" and 0 < y < n - 1 and 0 < x < m - 1:
                remaining = lines[y-1][x-1] + lines[y+1][x+1] + lines[y-1][x+1] + lines[y+1][x-1]
                if remaining in ["MSMS", "MSSM", "SMMS", "SMSM"]:
                    count += 1
    
    return count



if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))