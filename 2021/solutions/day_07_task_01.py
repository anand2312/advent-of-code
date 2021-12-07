import numpy as np
from typing import cast
from helpers import Puzzle


puzzle = Puzzle(day=7)


def main() -> int:
    positions = np.array(puzzle.raw_content.split(","), dtype=int)
    small = float('inf')

    for i in positions:
        fuel_needed = np.abs(positions - i).sum()
        if fuel_needed < small:
            small = fuel_needed
    
    return cast(int, small)


print(main())
