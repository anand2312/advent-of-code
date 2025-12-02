from helpers import Puzzle
from day_02_task_01 import parse
from functools import reduce, cache

puzzle = Puzzle(day=2)


@cache
def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def main(line: str) -> int:
    groups = parse(line)
    n = 0
    for group in groups:
        low, high = int(group[0]), int(group[1])
        for i in range(low, high + 1):
            as_str = str(i)
            possible_lens = factors(len(as_str))
            for factor in possible_lens:
                if factor <= len(as_str) // 2 and as_str == as_str[:factor] * int(len(as_str) / factor):
                    n += i
                    break
    return n


if __name__ == "__main__":
    print(main(puzzle.sample()))
    print(main(puzzle.raw_content))