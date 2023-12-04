from collections import Counter
from helpers import Puzzle
from day_04_task_01 import Card, parse


def common(card: Card) -> int:
    winning, has = card
    return len(set(winning).intersection(has))


def main(lines: list[str]) -> int:
    cards = parse(lines)
    counts = Counter(cards.keys())
    for k, v in cards.items():
        for i in range(k + 1, k + common(v) + 1):
            counts[i] += counts[k]
    return sum(counts.values())


if __name__ == "__main__":
    puzzle = Puzzle(day=4)
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))
