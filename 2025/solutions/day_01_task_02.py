from helpers import Puzzle


puzzle = Puzzle(day=1)


def main(lines: list[str]) -> int:
    count, current = 0, 50
    for line in lines:
        side, n = line[0], int(line[1:])
        sign = -1 if side == "L" else 1
        current, zeroes = turn_left(current, n) if sign == -1 else turn_right(current, n)
        count += zeroes
    return count

# lmao bruteforced it
def turn_left(current: int, n: int) -> tuple[int, int]:
    count = 0
    for _ in range(n):
        current -= 1
        if current == -1:
            current = 99
        if current == 0:
            count += 1
    return current, count


def turn_right(current: int, n: int) -> tuple[int, int]:
    count = 0
    for _ in range(n):
        current += 1
        if current == 100:
            current = 0
        if current == 0:
            count += 1
    return current, count


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))