from collections import Counter
from functools import cmp_to_key, partial
from typing import Callable
from helpers import Puzzle


Hand = tuple[str, int]


def card_kind(h: Hand) -> int:
    # Returns:
    # 5 - 5 of a kind
    # 4 - 4 of a kind
    # 3 - full house
    # 2 - three of a kind
    # 1 - two pair
    # 0 - one pair
    # -1 - high card
    c = Counter(h[0])
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


def compare(
    h1: Hand, h2: Hand, char_map: dict[str, int], kind: Callable[[Hand], int]
) -> int:
    k1, k2 = kind(h1), kind(h2)
    if k1 > k2:
        return 1
    elif k1 == k2:
        # same kind of hand - start comparing characters
        l1, l2 = (
            list(map(lambda i: char_map.get(i, int(i) if i.isdigit() else -1), h1[0])),
            list(map(lambda i: char_map.get(i, int(i) if i.isdigit() else -1), h2[0])),
        )
        if l1 > l2:
            return 1
        elif list(l1) == list(l2):
            return 0
        else:
            return -1
    else:
        return -1


def parse(lines: list[str]) -> list[Hand]:
    out = []
    for line in lines:
        card, bid = line.split()
        out.append((card, int(bid)))
    return out


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
                        char_map={"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10},
                        kind=card_kind,
                    )
                ),
            )
        )
    )


if __name__ == "__main__":
    puzzle = Puzzle(day=7)
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))
