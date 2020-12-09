"""Advent of Code Day 9"""
from utils import get_data
from itertools import combinations

data = get_data("XMAS")

# first 25 numbers are 'preamble'
# every number after that should be a sum of any two of previous 25 numbers
# find first number that doesn't follow this rule

def main(data: list) -> int:
    found = False
    low, high, current = 0, 26, 26
    while not found:
        # checking should start from the 26th number onwards i.e index 25
        current_element = data[current]
        sums = {sum(i) for i in combinations(data[low:high], 2)}
        if current_element not in sums:
            found = True    # unnecessary, directly returning will work
            return current_element
        else:
            low += 1
            high += 1
            current += 1

print(main(data))