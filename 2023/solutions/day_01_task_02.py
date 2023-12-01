import re

from helpers import Puzzle


puzzle = Puzzle(day=1)
nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
patterns = {re.compile(f"^{key}"): val for key, val in nums.items()}


def main(lines: list[str]) -> int:
    total = 0
    for line in lines:
        tens, ones = None, None
        line_len = len(line)
        for idx, char in enumerate(line):
            if char.isdigit():
                if tens is None:
                    tens = int(char)
                ones = int(char)
            else:
                for pattern in patterns:
                    if re.match(pattern, line[idx:]):
                        if tens is None:
                            tens = patterns[pattern]
                        ones = patterns[pattern]
        assert tens
        assert ones
        total += tens * 10 + ones
    return total

if __name__ == "__main__":
    sample = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    print(main(sample.splitlines()))
    print(main(puzzle.lines()))
        
                        
