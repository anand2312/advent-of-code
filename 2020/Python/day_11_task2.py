"""Advent of Code Day 11"""
from contextlib import suppress
from typing import Union
from utils import get_data
from day_11_task1 import Coordinates, Result, SeatingArrangement

data = list(map(list, get_data("seats")))

class NewSeatingArrangement(SeatingArrangement):
    def diagonal_right(self, coords: Coordinates, up: bool) -> Union[None, str]:
        found = False

        if up:
            row_diff = +1
        else:
            row_diff = -1

        old_row, old_column = coords

        with suppress(IndexError):
            while not found:
                new_row = old_row + row_diff
                new_column = old_column + 1

                if new_row < 0:
                    return

                next_element = self.seats[new_row][new_column]

                if next_element != ".":
                    found = True
                    return next_element
                else:
                    old_row, old_column = new_row, new_column

    def diagonal_left(self, coords: Coordinates, up: bool) -> Union[None, str]:
        found = False

        if up:
            row_diff = +1
        else:
            row_diff = -1

        old_row, old_column = coords

        with suppress(IndexError):
            while not found:
                new_row = old_row + row_diff
                new_column = old_column - 1

                if new_column < 0 or new_row < 0:
                    return

                next_element = self.seats[new_row][new_column]

                if next_element != ".":
                    found = True
                    return next_element
                else:
                    old_row, old_column = new_row, new_column

    def left(self, coords: Coordinates) -> Union[None, str]:
        found = False

        row, old_column = coords

        with suppress(IndexError):
            while not found:
                new_column = old_column - 1

                if new_column < 0:
                    return

                next_element = self.seats[row][new_column]

                if next_element != ".":
                    found = True
                    return next_element
                else:
                    old_column = new_column

    def right(self, coords: Coordinates) -> Union[None, str]:
        found = False

        row, old_column = coords

        with suppress(IndexError):
            while not found:
                new_column = old_column + 1

                next_element = self.seats[row][new_column]

                if next_element != ".":
                    found = True
                    return next_element
                else:
                    old_column = new_column

    def up(self, coords: Coordinates) -> Union[None, str]:
        found = False

        old_row, column = coords
        
        with suppress(IndexError):
            while not found:
                new_row = old_row - 1

                if new_row < 0:
                    return
                
                next_element = self.seats[new_row][column]

                if next_element != ".":
                    found = True
                    return next_element
                else:
                    old_row = new_row

    def down(self, coords: Coordinates) -> Union[None, str]:
        found = False

        old_row, column = coords
        
        with suppress(IndexError):
            while not found:
                new_row = old_row + 1

                next_element = self.seats[new_row][column]

                if next_element != ".":
                    found = True
                    return next_element
                else:
                    old_row = new_row

    def __getitem__(self, position: Coordinates) -> Result:
        # reimplementing getitem dunder to now return visible neighbors instead of just neighbors

        visible_neighbors = [
            self.diagonal_left(position, up=True),
            self.up(position),
            self.diagonal_right(position, up=True),
            self.right(position),
            self.diagonal_right(position, up=False),
            self.down(position),
            self.diagonal_left(position, up=False),
            self.left(position)
        ]

        item = self.seats[position.row][position.column]

        return Result(item=item, neighbors=visible_neighbors)


    @classmethod
    def transform(cls, old: "NewSeatingArrangement") -> "NewSeatingArrangement":
        # new rule - if 5 or more VISIBLE occupied seats make an occupied seat empty
        new = []

        for i in range(97):
            new_row = []
            for j in range(90):
                coords = Coordinates(row=i, column=j)
                old_item, old_neigbors = old[coords]

                if old_item == "L":
                    if "#" not in old_neigbors:
                        new_row.append("#")
                    else:
                        new_row.append("L")
                elif old_item == "#":
                    if old_neigbors.count("#") >= 5:
                        new_row.append("L")
                    else:
                        new_row.append("#")
                else:
                    new_row.append(old_item)
            else:
                new.append(new_row)

        return cls(new)

if __name__ == "__main__":
    old = NewSeatingArrangement(data)
    changed = True

    while changed:
        new = NewSeatingArrangement.transform(old)
        if old != new:
            old = new
            continue
        else:
            changed = False
            print(new.counts()["occupied"])
