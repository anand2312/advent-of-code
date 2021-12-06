import numpy as np
from helpers import Puzzle


puzzle = Puzzle(day=6)


def main(days: int = 80) -> int:
    """Calculate how many fish exist after 80 days."""
    fish = np.array(puzzle.raw_content.split(","), dtype=int)

    while days >= 1:
        fish -= 1
        reproduced = abs(fish[fish == -1].sum())
        fish[fish == -1] = 6
        fish = np.append(fish, [8] * int(reproduced))
        days -= 1
    
    return len(fish)

if __name__ == "__main__":
    print(main(80))
