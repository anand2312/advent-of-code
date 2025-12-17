from helpers import Puzzle


puzzle = Puzzle(day=7)


def main(lines: list[str]) -> int:
    arr = [0 if i == "." else 1 for i in lines[0]]
    n = len(arr)
    count = 0
    for (y, line) in enumerate(lines[1:]):
        for (x, char) in enumerate(line):
            if char == "^":
                if arr[x]:
                    # light beam encountered splitter
                    count += 1
                    # beam gets split - so it doesn't continue on this path
                    arr[x] = 0
                    if x >= 1:
                        # left side
                        arr[x-1] = 1
                    if x <= n - 2:
                        # right side
                        arr[x+1] = 1
    
    return count


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))