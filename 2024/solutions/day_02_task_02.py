from helpers import Puzzle
from day_02_task_01 import safe

puzzle = Puzzle(day=2)


def main(lines: list[str]) -> int:
    reports = [[int(i) for i  in line.split()] for line in lines]
    count = 0

    for report in reports:
        if safe(report):
            count += 1
        else:
            for c in range(0, len(report)):
                if safe(report[:c] + report[c+1:]):
                    count += 1
                    break
    
    return count


if __name__ == "__main__":
    sample = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    print(main(sample.splitlines()))
    print(main(puzzle.lines()))