"""Advent of Code Day 5"""
from day_5_task1 import find_row, find_column, seat_id
from utils import get_data

data = get_data("boarding-pass")

def main() -> None:
    _id = set()
    for bpass in data:
        row, column = find_row(bpass), find_column(bpass)
        _id.add(seat_id(row, column))
    print(set(range(min(_id), max(_id)+1)) - _id)

main()