from collections import Counter
from helpers import Puzzle


puzzle = Puzzle(day=3)
lines = puzzle.lines()
length = len(lines[0])
gamma = []  # most common bit


for i in range(length):
    counter = Counter([line[i] for line in lines])
    most_common = counter.most_common(1)[0][0]
    gamma.append(most_common)

epsilon = [str(int(not i)) for i in map(int, gamma)]  # get the opposite bit for each bit in gamma

gamma = int(''.join(gamma), base=2)
epsilon = int(''.join(epsilon), base=2)

print(gamma * epsilon)
