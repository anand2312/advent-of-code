"""Advent of Code Day 12"""
from utils import get_data
from day_12_task1 import manhattan_distance, Ferry

data = get_data("ferry instructions")

class NewFerry(Ferry):
    # rewrote almost the entire class
    def __init__(self, instructions: list):
        self.instructions = instructions
        self.waypoint = 10 + 1j
        self.coords = 0 + 0j   # ship, not the waypoint

    def vertical(self, amount: int, up: bool) -> None:
        if up:
            new = complex(0, amount)
        else:
            new = complex(0, -amount)

        self.waypoint += new
    
    def horizontal(self, amount: int, right: bool) -> None:
        if right:
            new = complex(amount, 0)
        else:
            new = complex(-amount, 0)
        
        self.waypoint += new

    def turn(self, dir: str, amount: int) -> None:
        if dir == "R":
            amount = 360 - amount

        rel = self.coords - self.waypoint

        if amount == 90:
            rel *= 0 + 1j
        elif amount == 180:
            rel *= -1
        elif amount == 270:
            rel *= 0 - 1j

        self.waypoint = self.coords - rel
        
    def front(self, amount: int) -> None:
        old_waypoint = self.waypoint
        rel = self.waypoint - self.coords
        self.coords += rel * amount
        self.waypoint = self.coords + rel

def main() -> int:
    ferry = NewFerry(data)
    ferry.run()
    manhattan = manhattan_distance(ferry.coords)
    print(manhattan)
    return manhattan

main()
