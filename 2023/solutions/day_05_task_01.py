from collections import defaultdict
import re
from typing import NamedTuple

from helpers import Puzzle


class Mapping(NamedTuple):
    src: str
    dest: str
    src_start: int
    dest_start: int
    size: int


Seeds = list[int]


def parse(data: str) -> tuple[Seeds, dict[str, list[Mapping]]]:
    groups = data.split("\n\n")
    seeds = [int(i) for i in re.findall(r"\d+", groups[0])]
    maps = defaultdict(list)
    for grp in groups[1:]:
        lines = grp.splitlines()
        m = re.match(r"(?P<src>[a-z]+)-to-(?P<dst>[a-z]+)", lines[0])
        if not m:
            raise ValueError(f"Line {lines[0]} did not match pattern")
        src, dest = m.group("src"), m.group("dst")
        for line in lines[1:]:
            dest_start, src_start, size = [int(i) for i in line.strip().split()]
            maps[src].append(
                Mapping(
                    src=src,
                    dest=dest,
                    src_start=src_start,
                    dest_start=dest_start,
                    size=size,
                )
            )
    return seeds, maps


def seed_to_location(n: int, maps: dict[str, list[Mapping]]) -> int:
    curr_src = "seed"
    curr = n
    while curr_src != "location":
        for m in maps[curr_src]:
            if m.src_start <= curr <= m.src_start + m.size:
                diff = curr - m.src_start
                # print(f"{curr_src} to {m.dest}")
                # print(f"{m=} {curr=} maps to {m.dest_start + diff}")
                curr = m.dest_start + diff
                curr_src = m.dest
                break
        else:
            curr_src = maps[curr_src][0].dest
    return curr


def main(data: str) -> int:
    seeds, maps = parse(data)
    return min([seed_to_location(i, maps) for i in seeds])


if __name__ == "__main__":
    puzzle = Puzzle(day=5)
    print(main(puzzle.sample()))
    print(main(puzzle.raw_content))
