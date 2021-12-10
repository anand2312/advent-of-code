from helpers import Puzzle


puzzle = Puzzle(day=10)

OPENING = {"(", "[", "{", "<"}
CLOSING_TO_OPENING = {"]": "[", ")": "(", "}": "{", ">": "<"}
OPENING_TO_CLOSING = {"[": "]", "(": ")", "{": "}", "<": ">"}
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}


def parse_line(ln: str) -> str:
    """
    Parses a line, and returns the first faulty character
    if the line is corrupted, or the string -1 if it is
    incomplete.
    """
    stack = []

    for char in ln:
        if char in OPENING:
            stack.append(char)
        else:
            opening = stack.pop()
            if CLOSING_TO_OPENING[char] == opening:
                continue
            else:
                return char # corrupted line
    else:
        return "-1"


def main() -> int:
    score = 0
    for line in puzzle.lines():
        res = parse_line(line)

        if res == "-1":
            continue
        else:
            score += POINTS[res]
    return score


if __name__ == "__main__":
    print(main())
