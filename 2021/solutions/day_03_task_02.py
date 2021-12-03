from collections import Counter
from typing import Literal
from helpers import Puzzle


puzzle = Puzzle(day=3)
lines = puzzle.lines()

length = len(lines[0])


def get_criteria_at(pos: int, nums: list[str], _type: Literal["o2", "co2"]) -> str:
    counter = Counter([line[pos] for line in nums])
    ones, zeroes = counter['1'], counter['0']
    most = max(counter.keys(), key=lambda i: counter[i])
    least = min(counter.keys(), key=lambda i: counter[i])

    if ones == zeroes:
        return '1' if _type == "o2" else '0'
    
    return most if _type == "o2" else least

def filter_numbers(bytes: list[str], i: int, type_: Literal["o2", "co2"]) -> str:
    criteria = get_criteria_at(i, bytes, type_)
    filtered = [byte for byte in bytes if byte[i] == criteria]

    if len(filtered) == 1:
        return filtered[0]
    else:
        return filter_numbers(filtered, i + 1, type_)

def main() -> int:
    o2, co2 = int(filter_numbers(lines, 0, "o2"), base=2), int(filter_numbers(lines, 0, "co2"), base=2)
    return o2 * co2

print(main())