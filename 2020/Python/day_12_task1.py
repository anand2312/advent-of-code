"""Advent of Code Day 12"""
from utils import get_data

data = get_data("ferry instructions")
            
class Ferry:
    def __init__(self, instructions: list):
        self.instructions: list = instructions
        self.facing: Direction = Direction("east")
        self.coords: complex = 0 + 0j

    def vertical(self, amount: int, up: bool) -> None:
        if up:
            new = complex(0, amount)
        else:
            new = complex(0, -amount)
        self.coords += new

    def horizontal(self, amount: int, right: int) -> None:
        if right:
            new = complex(amount, 0)
        else:
            new = complex(-amount, 0)
        self.coords += new

    def turn(self, direction: str, angle: int) -> None:
        """To turn 90 degrees - multiply by i"""
        if direction == "R":
            angle = 360 - angle

        self.facing += angle   # stupid, you wrote the right way to do this in the comment and then made a stupid class. wow.

    def front(self, amount: int) -> None:
        if self.facing.direction == "east":
            new = complex(amount, 0)
        elif self.facing.direction == "west":
            new = complex(-amount, 0)
        elif self.facing.direction == "north":
            new = complex(0, amount)
        else:
            new = complex(0, -amount)

        self.coords += new

    def run(self) -> int:
        for instruction in self.instructions:
            dir, amount = instruction[0], int(instruction[1:])

            if dir == "N":
                self.vertical(amount, up=True)
            elif dir == "S":
                self.vertical(amount, up=False)
            elif dir == "E":
                self.horizontal(amount, right=True)
            elif dir == "W":
                self.horizontal(amount, right=False)
            elif dir in {"L", "R"}:
                self.turn(dir, amount)
            elif dir == "F":
                self.front(amount)


class Direction:
    def __init__(self, dir: str):
        self.direction = dir

    def __add__(self, angle: int) -> "Direction":
        if angle == 90:
            if self.direction == "north":
                self.direction = "west"
            elif self.direction == "west":
                self.direction = "south"
            elif self.direction == "south":
                self.direction = "east"
            else:
                self.direction = "north"
        elif angle == 180:
            if self.direction == "north":
                self.direction = "south"
            elif self.direction == "west":
                self.direction = "east"
            elif self.direction == "south":
                self.direction = "north"
            else:
                self.direction = "west"
        elif angle == 270:
            if self.direction == "north":
                self.direction = "east"
            elif self.direction == "west":
                self.direction = "north"
            elif self.direction == "south":
                self.direction = "west"
            else:
                self.direction = "south"
        return self
        
def manhattan_distance(coords: complex) -> int:
    return sum(map(abs, [coords.real, coords.imag]))

def main() -> None:
    ferry = Ferry(data)
    ferry.run()
    print(manhattan_distance(ferry.coords))
