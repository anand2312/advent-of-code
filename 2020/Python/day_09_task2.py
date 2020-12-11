"""Advent of Code Day 9"""
from utils import get_data
from day_09_task1 import main as find_invalid_number
from itertools import accumulate
import operator

data = get_data("XMAS")
invalid_number = find_invalid_number(data)

# accumulate function applies the function passed in, one by one on the items of the iterable, returning a new iterable with the output of that function (see example)
""" for example;
L = [1, 2, 3, 4, 5]
accumulate(L, add) -> 1, 3, 6, 10, 15   (each number being added to sum of all previous numbers)
"""

def main(data: list, invalid: int) -> int:
    for index, start_element in enumerate(data):
        contiguous_sums = list(accumulate(data[index:], operator.add))
        for sum_index, sum_ in enumerate(contiguous_sums):
            if invalid == sum_:
                # index in the contiguous sums array will be the upper limit of the contiguous slice from the slice data[index:]. so the corresponding index in the original array will be sum_index + index
                contiguous_slice = data[index: sum_index + index + 1]
                return sum([min(contiguous_slice), max(contiguous_slice)])

if __name__ == "__main__":                   
    print(main(data, invalid_number))


