from helpers import Puzzle
from day_05_task_01 import parse_rules, valid_update
from functools import cmp_to_key


puzzle = Puzzle(day=5)


def main(lines: str) -> int:
    rules, updates = lines.split("\n\n")
    before, after = parse_rules(rules.splitlines())

    def compare_rules(r1, r2) -> int:
        if r1 in before[r2]:
            return -1
        elif r1 in after[r2]:
            return 1
        else:
            return 0

    out = 0

    for update in [i.split(",") for i in updates.splitlines()]:
        size = len(update)
        if not valid_update(update, before, after):
            out += int(sorted(update, key=cmp_to_key(compare_rules))[size // 2])
    
    return out


if __name__ == "__main__":
    print(main(puzzle.sample()))
    print(main(puzzle.raw_content))