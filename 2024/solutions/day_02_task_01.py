from helpers import Puzzle

puzzle = Puzzle(day=2)

def safe(report: list[int]) -> bool:
    diff = report[0] - report[1]
    if abs(diff) < 1 or abs(diff) > 3:
        return False
    flag = diff >= 0

    for i in range(1, len(report) - 1):
        diff = report[i] - report[i+1]
        sign = diff >= 0
        if sign is not flag:
            return False
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    
    return True
    

def main(lines: list[str]) -> int:
    count = 0
    for line in lines:
        if safe([int(i) for i in line.split()]):
            count += 1
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
