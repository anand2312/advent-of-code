"""Advent of Code Day 1"""
from utils import get_data

report = get_data('report')
for i in report:
    if (j := 2020 - i) in report:
        print(i * j)