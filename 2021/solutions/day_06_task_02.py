from collections import Counter, defaultdict
from helpers import Puzzle


puzzle = Puzzle(day=6)
# part 1 solution was naive and will run until the heat death of the universe, you need to do better

starting_fish = [int(i) for i in puzzle.raw_content.split(",")]
counter = Counter(starting_fish)


for day in range(256):
    next_iter = defaultdict(int)

    for days_left, count in counter.items():
        if days_left == 0:
            next_iter[6] += count
            next_iter[8] += count
        else:
            next_iter[days_left - 1] += count
    
    counter = next_iter

print(sum(counter.values()))
