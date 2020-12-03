from day_3_task1 import raw_data, total_rows
import math

# Reimplimenting the index incrementers to work with any increment. Should've done this in the other file :/
def custom_vertical_inc(old: int, down: int, total_rows: int=total_rows) -> int:
    if old == total_rows - 1:
        raise IndexError
    else:
        return old + down

def custom_horizontal_inc(old: int, right: int) -> int:
    new = old + right
    if new > 30:
        return new - 31
    else:
        return new

def count_trees(shifts: tuple, raw_data=raw_data) -> int:
    right_shift, down_shift = shifts
    ver, hor = 0, 0
    trees = 0
    try:
        while True:
            if raw_data[ver][hor] == "#":
                trees += 1
            ver, hor = custom_vertical_inc(ver, down_shift), custom_horizontal_inc(hor, right_shift)
    except IndexError:
        return trees

# solution is product of trees found for a set of slopes (right x down y)

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(math.prod(map(count_trees, slopes)))



