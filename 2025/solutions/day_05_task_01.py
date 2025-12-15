from helpers import Puzzle
from ranges import Range

puzzle = Puzzle(day=5)


def main(lines: list[str]) -> int:
    fresh = set()
    avl_ids_idx = 0

    for (idx, line) in enumerate(lines):
        if line == "":
            avl_ids_idx = idx
            break
        low, high = [int (i) for i in line.split("-")]
        fresh.add(Range(low, high, include_end=True))

    count = 0
    for line in lines[avl_ids_idx + 1:]:
        if any(int(line) in r for r in fresh):
            count += 1
    
    return count


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))