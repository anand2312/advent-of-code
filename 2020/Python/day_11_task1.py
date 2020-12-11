"""Advent of Code Day 11"""
from utils import get_data
from collections import namedtuple

data = list(map(list, get_data("seats")))
# data is now in the form of a list of lists

Coordinates = namedtuple("Coordinates", "row column")
Result = namedtuple("Result", "item neighbors")

"""
L - empty
. - floor 
# - occupied
"""

class SeatingArrangement:
    def __init__(self, seats: list):
        self.seats = seats

    def counts(self) -> dict:
        occupied, empty, floor = 0, 0, 0

        for row in self.seats:
            occupied += row.count("#")
            empty += row.count("L")
            floor += row.count(".")

        return {"occupied": occupied, "empty": empty, "floor": floor}

    def __getitem__(self, position: Coordinates) -> Result:
        surrounding_indices = set()
        neighbors = list()
        
        for i in range(position.column-1, position.column+2):
            surrounding_indices.update([Coordinates(position.row-1, i), Coordinates(position.row+1, i)])
            
        surrounding_indices.update([Coordinates(position.row, position.column-1), Coordinates(position.row, position.column+1)])

        filter_results = lambda coordinate: (coordinate.row >= 0) and (coordinate.column >= 0) and (coordinate.column <= 89) and (coordinate.row <= 96)

        surrounding_indices = filter(filter_results, surrounding_indices)

        for i in surrounding_indices:
            neighbors.append(self.seats[i.row][i.column])

        return Result(item=self.seats[position.row][position.column], neighbors=neighbors)
  
    def __eq__(self, other) -> bool:
        return self.seats == other.seats

    @classmethod
    def transform(cls, old: "SeatingArrangement") -> "SeatingArrangement":
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
                    if old_neigbors.count("#") >= 4:
                        new_row.append("L")
                    else:
                        new_row.append("#")
                else:
                    new_row.append(old_item)
            else:
                new.append(new_row)

        return cls(new)


if __name__ == "__main__":
    old = SeatingArrangement(data)
    changed = True

    while changed:
        new = SeatingArrangement.transform(old)
        if old != new:
            old = new
            continue
        else:
            changed = False
            print(new.counts()["occupied"])