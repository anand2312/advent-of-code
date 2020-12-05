"""Advent of Code Day 5"""
from utils import get_data, odd

# data is now in the form of a list of strings
# where each string is a boarding pass
data = get_data("boarding-pass")

def find_row(bpass: str, low: int=0, up: int=127, curr: int=0) -> int:
    # F - lower
    # B - upper
    if low == (up - 1):
        if bpass[curr] == "F":
            return low
        else:
            return up
    else:
        if bpass[curr] == "F":
            return find_row(bpass, low, ((up+low)//2), curr+1)
        elif bpass[curr] == "B":
            return find_row(bpass, ((up+low)//2), up, curr+1)

def find_column(bpass: str) -> int:
    low, up = 0, 7
    for i in bpass[7:9]:
        if i == "L":
            if odd(low+up):
                up = (low+up)//2
            else:
                up = int((low+up)/2)
        else:
            if odd(low+up):
                low = (low+up)//2 + 1
            else:
                low = int((low+up)/2) + 1
    else:
        if bpass[9] == "L":
            return low
        else:
            return up

def seat_id(row: int, column: int) -> int:
    return (row * 8) + column

def main() -> None:
    ids = []
    for bpass in data:
        row, column = find_row(bpass), find_column(bpass)
        _id = seat_id(row=row, column=column)
        ids.append(_id)
    print(max(ids))
