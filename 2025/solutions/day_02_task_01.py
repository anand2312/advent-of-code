from helpers import Puzzle
import re

puzzle = Puzzle(day=2)


def parse(line: str) -> list[tuple[str, str]]:
    return re.findall(r"(?P<low>\d+)-(?P<hi>\d+)", line)


# Only d2p1 and I'm again bruteforcing :(
def main(line: str) -> int:
    groups = parse(line)
    n = 0
    for group in groups:
        low, hi = int(group[0]), int(group[1])
        for i in range(low, hi + 1):
            as_str = str(i)
            mid = len(as_str) // 2
            if as_str[:mid] == as_str[mid:]:
                n += i
    return n


if __name__ == "__main__":
    print(main(puzzle.sample()))
    print(main(puzzle.raw_content))