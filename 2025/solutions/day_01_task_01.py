from helpers import Puzzle


puzzle = Puzzle(day=1)


def main(lines: list[str]) -> int:
    count, current = 0, 50
    for line in lines:
        side, n = line[0], int(line[1:])
        sign = -1 if side == "L" else 1
        current = (current + (n * sign)) % 100
        if current == 0:
            count += 1
    return count


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))