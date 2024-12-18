from helpers import Puzzle
from collections import defaultdict


puzzle = Puzzle(day=5)


def parse_rules(rules: list[str]) -> tuple[dict[str, str], dict[str, str]]:
    before, after = defaultdict(list), defaultdict(list)

    for x, y in [rule.split("|") for rule in rules]:
        before[y].append(x)
        after[x].append(y)
    
    return before, after


def valid_update(update: list[str], before: dict[str, str], after: dict[str, str]) -> bool:
    for idx, page in enumerate(update):
        if not (set(before[page]).issuperset(update[:idx]) and set(after[page]).issuperset(update[idx+1:])):
            return False
    return True


def main(lines: str) -> int:
    rules, updates = lines.split("\n\n")
    before, after = parse_rules(rules.splitlines())

    out = 0

    for update in [i.split(",") for i in updates.splitlines()]:
        size = len(update)
        if valid_update(update, before, after):
            out += int(update[size // 2])
    
    return out


if __name__ == "__main__":
    print(main(puzzle.sample()))
    print(main(puzzle.raw_content))