from helpers import Puzzle

Card = tuple[list[int], list[int]]


def parse(lines: list[str]) -> dict[int, Card]:
    out: dict[int, Card] = {}
    for line in lines:
        card, rest = line.split(": ")
        card_no = int(card[5:])
        winning, has = rest.split(" | ")
        winning = [int(i) for i in winning.split()]
        has = [int(i) for i in has.split()]
        out[card_no] = winning, has
    return out


def card_points(card: Card) -> int:
    winning, has = card
    common = len(set(winning).intersection(has))
    return pow(2, common - 1) if common > 0 else 0


def main(lines: list[str]) -> int:
    cards = parse(lines)
    points = [card_points(v) for v in cards.values()]
    return sum(points)


if __name__ == "__main__":
    puzzle = Puzzle(day=4)
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))
