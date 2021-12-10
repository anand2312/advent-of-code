from helpers import Puzzle
from day_10_task_01 import CLOSING_TO_OPENING, OPENING, OPENING_TO_CLOSING


puzzle = Puzzle(day=10)
POINTS = {")": 1, "]": 2, "}": 3, ">": 4}


def parse_line(ln: str) -> str:
    """
    Parses a line, but this time returns the
    characters missing in an incomplete line
    and return -1 if the line is corrupted.
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
                return "-1"  # corrupted line
    else:
        return "".join([OPENING_TO_CLOSING[i] for i in stack[::-1]])


def main() -> int:
    scores = []
    for line in puzzle.lines():
        res = parse_line(line)

        if res == "-1":
            continue

        score = 0

        for char in res:
            score *= 5
            score += POINTS[char]
        
        scores.append(score)

    scores = sorted(scores)
    mid = (len(scores) - 1) // 2
    return scores[mid]


if __name__ == "__main__":
    print(main())
