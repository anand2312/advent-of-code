"""Advent of Code Day 3"""
from utils import get_data

raw_data = get_data("trees")
total_rows = len(raw_data)
trees = 0
# the map is now in the form of a list,
# with each row being a string 

def inc_horizontal_index(old: int) -> int:
    if old == 28:   
        return 0
    elif old == 29:
        return 1
    elif old == 30:
        return 2
    else:
        return old + 3

def inc_vertical_index(old: int) -> int:
    global total_rows
    if old == total_rows - 1:
        raise IndexError # puzzle ends here
    else:
        return old + 1

if __name__ == "__main__":
    ver, hor = 0, 0    #  starting coordinates
    try:
        while True:
            if raw_data[ver][hor] == "#":
                trees += 1
            ver, hor = inc_vertical_index(ver), inc_horizontal_index(hor)
    except IndexError:
        print(trees)
    
