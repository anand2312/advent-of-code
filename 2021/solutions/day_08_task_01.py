from typing import List, Tuple
from helpers import Puzzle


puzzle = Puzzle(day=8)
ParsedLine = Tuple[List[str], List[str]]


def parse_line(ln: str) -> ParsedLine:
    a, b = [i.split() for i in ln.split(" | ")]
    return a, b


def parse_input(raw: str) -> List[ParsedLine]:
    return [*map(parse_line, raw.splitlines())]


def main(raw: str) -> int:
    lines = parse_input(raw)
    count = 0

    for _, output in lines:
        for pattern in output:
            if len(pattern) in {2, 4, 3, 7}:
                count += 1

    return count


if __name__ == "__main__":
    raw = puzzle.raw_content
    print(main(raw))
