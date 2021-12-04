from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
from numpy.lib.arraysetops import isin
import numpy.typing as npt

from helpers import Puzzle


puzzle = Puzzle(day=4)


@dataclass
class Position:
    num: int
    marked: bool = False

    def __bool__(self) -> bool:
        # used during ANY/ALL checking
        return self.marked
    
    def __add__(self, other: "Position") -> "Position":
        # used in the end while summing
        # return a Position object to allow the array
        # to be passed into sum()
        # access the actual sum with
        # pos.num
        return Position(self.num + other.num)

BoardType = List[npt.NDArray]
CallNumbers = List[int]
AllPositions = Dict[int, Position]


def parse_input() -> Tuple[CallNumbers, BoardType, AllPositions]:
    split = puzzle.raw_content.split("\n\n") # break whenever there's an empty line in between
    call_numbers = [int(i) for i in split[0].split(",")]  # the very first line are the numbers to call
    # make only a single Position object for each number in the call order
    # and put these instances on the boards
    # this makes it easy to simply flip the "done" marker for one instance
    # and it is updated across all boards
    positions = {i: Position(num=i) for i in call_numbers}
    boards = []

    for unparsed_board in split[1:]:  # the rest are all bingo boards
        # split the unparsed board at each line
        # then split each line at a space, convert each number to int, and add the Position object
        board = [[positions[int(i)] for i in line.split()] for line in unparsed_board.splitlines()]
        boards.append(np.array(board))
    
    return call_numbers, boards, positions


def check_if_win(board: npt.NDArray) -> bool:
    """Takes a board as input and returns True if it is in a winning condition."""
    rows = np.any(np.all(board, 1))
    if rows:
        return True
    cols = np.any(np.all(board, 0))
    if cols:
        return True
    return False


def main() -> int:
    nums, boards, positions = parse_input()

    for num in nums:
        pos_obj = positions[num]
        # mark the position as called
        pos_obj.marked = True

        # check if any board has won
        for board in boards:
            if check_if_win(board):
                # calculate sum of unmarked positions
                unmarked_sum = sum(i.num for i in board.ravel() if not i.marked)
                # the answer is the number that was just called
                # multiplied by the unmarked sum
                return num * unmarked_sum
    else:
        return -1 # fail case, only to appease type system


print(main())
