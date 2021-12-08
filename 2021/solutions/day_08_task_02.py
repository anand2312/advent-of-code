from typing import Dict, List, Tuple, Union
from helpers import Puzzle
from day_08_task_01 import parse_input, ParsedLine


puzzle = Puzzle(day=8)


def solve_line(line: ParsedLine) -> int:
    """Figure out the connections for a single line and return it's output number."""
    num_to_pattern: Dict[
        Union[int, Tuple[int, int, int]], Union[str, List[str]]
    ] = {}  # keep track of the segments needed for each number

    num_of_segs_to_num = {
        6: (0, 6, 9),
        5: (2, 3, 5),
    }  # get which number it could possibly be, based on the number of segments it has

    for num_pattern in line[0]:
        # first figure out the ones we can definitely know
        # like 1: 2 segs, 4: 4 segs, 7: 3 segs, 8: 7 segs
        length = len(num_pattern)
        if length == 2:
            num_to_pattern[1] = num_pattern
        elif length == 4:
            num_to_pattern[4] = num_pattern
        elif length == 3:
            num_to_pattern[7] = num_pattern
        elif length == 7:
            num_to_pattern[8] = num_pattern
        else:
            possible_nums = num_of_segs_to_num[length]
            # get the list of possible patterns for this set of numbers
            if (j := num_to_pattern.get(possible_nums)) is None:
                # if it doesn't exist, create the list
                num_to_pattern[possible_nums] = [num_pattern]
            else:
                if isinstance(j, list):
                    j.append(num_pattern)

    # get fucked, write the shittiest solution possible
    # given the pattern 1, and taking the 3 possible patterns with length 6,
    # we can figure out the pattern for 6
    # do this kind of shit for every number

    for possible_pattern in num_to_pattern[(0, 6, 9)]:
        if len(set(possible_pattern) & set(num_to_pattern[1])) == 1:
            # only happens for 6 out of these three
            num_to_pattern[6] = possible_pattern
        else:
            if len(set(possible_pattern) & set(num_to_pattern[4])) == 3:
                # only happens for 0 out of these three
                num_to_pattern[0] = possible_pattern
            else:
                num_to_pattern[9] = possible_pattern
    else:
        # now remove the 0, 6, 9 list as we're sure of their patterns
        num_to_pattern.pop((0, 6, 9))

    for possible_pattern in num_to_pattern[(2, 3, 5)]:
        if len(set(possible_pattern) & set(num_to_pattern[1])) == 2:
            # only happens for 3 out of these three
            num_to_pattern[3] = possible_pattern
        else:
            if len(set(possible_pattern) & set(num_to_pattern[6])) == 5:
                # only happens for 5
                num_to_pattern[5] = possible_pattern
            else:
                num_to_pattern[2] = possible_pattern
    else:
        num_to_pattern.pop((2, 3, 5))

    out = ""

    for pattern in line[1]:
        # now go through the output patterns and figure out what the number is
        for num, num_pattern in num_to_pattern.items():
            # the output pattern may not be in the same order as the pattern we calculated
            if set(pattern) == set(num_pattern):
                out += str(num)

    return int(out)


def main(raw: str) -> int:
    lines = parse_input(raw)
    return sum(solve_line(ln) for ln in lines)


if __name__ == "__main__":
    raw = puzzle.raw_content
    print(main(raw))
