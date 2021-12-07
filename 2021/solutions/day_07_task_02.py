import numpy as np
from helpers import Puzzle


puzzle = Puzzle(day=7)


def main() -> int:
    positions = np.array(puzzle.raw_content.split(","), dtype=int)
    small = float('inf')

    # now we need to consider positions
    # that AREN'T already occupied by some submarine    
    for i in range(positions.max()):
        diff = np.abs(positions - i)
        fuel_needed = (diff * (diff + 1) / 2).sum()
        if fuel_needed < small:
            small = fuel_needed
    
    return int(small)


print(main())
