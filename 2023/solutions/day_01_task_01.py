from helpers import Puzzle


puzzle = Puzzle(day=1)


def main(lines: list[str]) -> int:
    total = 0
    for line in lines:
        tens, ones = None, None
        for char in line:
            if char.isdigit():
                if tens is None:
                    tens = int(char)
                ones = int(char)
        assert tens
        assert ones
        total += tens * 10 + ones
    return total


if __name__ == "__main__":
    sample = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    print(main(sample.split()))
    print(main(puzzle.lines()))
