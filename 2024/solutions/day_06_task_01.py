from helpers import Puzzle


puzzle = Puzzle(day=6)


def main(lines: list[str]) -> int:
    n, m = len(lines), len(lines[0])
    lines = [list(line) for line in lines]
    start = complex(0, 0)

    for y in range(n):
        for x in range(m):
            if lines[y][x] == "^":
                start = complex(x, y)
                break
    
    curr = start
    direction = 0 - 1j
    visited = set()
    visited.add(curr)

    while 0 <= curr.real < m and 0 <= curr.imag < n:
        next_pos = curr + direction
        x, y = int(next_pos.real), int(next_pos.imag)
        if x < 0 or y < 0: break
        try:
            if lines[y][x] == "#":
                direction *= complex(0, 1)
            else:
                curr = next_pos
                visited.add(curr)
        except IndexError:
            break
    
    return len(visited)


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))