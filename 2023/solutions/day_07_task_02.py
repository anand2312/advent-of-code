from collections import Counter
from functools import cmp_to_key, partial
from helpers import Puzzle
from day_07_task_01 import Hand, compare, parse


def card_kind_with_joker(h: Hand) -> int:
    # Returns:
    # 5 - 5 of a kind
    # 4 - 4 of a kind
    # 3 - full house
    # 2 - three of a kind
    # 1 - two pair
    # 0 - one pair
    # -1 - high card
    c = Counter(h[0])
    jokers = c.get("J", 0)
    if jokers:
        most_common_key, _ = c.most_common(1)[0]
        if most_common_key == "J":
            # either the hand is JJJJJ
            # or it has mostly J's, but it has some
            # other characters too
            if len(c) == 1:
                # all Js - 5 of a kind
                return 5
            else:
                most_common_key, _ = c.most_common(2)[1]
        c[most_common_key] += jokers
        del c["J"]
    match c.most_common():
        case [(_, 5)]:
            return 5
        case [(_, 4), (_, 1)]:
            return 4
        case [(_, 3), (_, 2)]:
            return 3
        case [(_, 3), (_, 1), (_, 1)]:
            return 2
        case [(_, 2), (_, 2), (_, 1)]:
            return 1
        case [(_, 2), (_, 1), (_, 1), (_, 1)]:
            return 0
        case _:
            return -1


def main(lines: list[str]) -> int:
    cards = parse(lines)
    return sum(
        (idx + 1) * bid
        for idx, (_, bid) in enumerate(
            sorted(
                cards,
                key=cmp_to_key(
                    partial(
                        compare,
                        char_map={"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10},
                        kind=card_kind_with_joker,
                    )
                ),
            )
        )
    )


if __name__ == "__main__":
    puzzle = Puzzle(day=7)
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))
