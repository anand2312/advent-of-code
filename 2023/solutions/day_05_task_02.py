from helpers import Puzzle, chunks
from day_05_task_01 import Mapping, parse, seed_to_location


def range_intersection(r1: range, r2: range) -> range:
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop))


def range_difference(r1: range, r2: range) -> list[range]:
    # if r1 is denoted by () and r2 by []
    #   (...[.)..] -> remaining = (...[
    #   [...(.]..) -> remaining = ]..)
    #   [..(..)..] -> remaining = empty
    #   (..[..]..) -> remaining = (..[ and ]..)
    # does any of this make sense? i don't know how to put this
    # into words
    intersection = range_intersection(r1, r2)
    if intersection.start == r2.start:  # either case 1 or 4
        out = [range(r1.start, intersection.start)]
        if intersection.stop == r2.stop:
            # case 4
            out.append(range(intersection.stop, r1.stop))
    else:
        out = []
        if intersection.stop == r2.stop:
            # case 2
            out.append(range(intersection.stop, r1.stop))
    return [i for i in out if bool(i)]


def seed_to_location_range(
    ranges: list[range], curr: str, maps: dict[str, list[Mapping]]
) -> list[range]:
    if curr == "location":
        return ranges
    out = []
    for r in ranges:
        for m in maps[curr]:
            mr = range(m.src_start, m.src_start + m.size)
            if intersection := range_intersection(r, mr):
                diff = m.dest_start - m.src_start
                remaining = range_difference(r, mr)
                ranges.extend(remaining)
                out.append(range(intersection.start + diff, intersection.stop + diff))
                break
        else:
            out.append(r)
    out = [i for i in out if bool(i)]  # filter out empty ranges
    return seed_to_location_range(out, maps[curr][0].dest, maps)


def main(data: str) -> int:
    seeds, maps = parse(data)
    return min(
        min(
            i.start
            for i in seed_to_location_range([range(start, start + size)], "seed", maps)
        )
        for (start, size) in chunks(seeds, 2)
    )


if __name__ == "__main__":
    puzzle = Puzzle(day=5)
    print(main(puzzle.sample()))
    print(main(puzzle.raw_content))
