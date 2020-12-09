"""Advent of Code Day 9"""
from utils import get_data
from day_9_task1 import main as find_invalid_number
from itertools import accumulate
import operator

data = get_data("XMAS")
invalid_number = find_invalid_number(data)

# accumulate function applies the function passed in, in sequence on the iterable
""" for example;
L = [1, 2, 3, 4, 5]
accumulate(L, add) -> 1, 3, 6, 10, 15   (each number being added to sum of all previous numbers)
"""

def main(data) -> int:
    

