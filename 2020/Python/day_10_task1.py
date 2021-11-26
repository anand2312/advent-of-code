"""Advent of Code Day 10"""
from utils import get_data

data = get_data("adapters")

def main(data: list) -> list:
    differences = []
    data = sorted(data)

    device = data[-1] + 3
    prev = 0

    # can only connect if the previous jolt is 1-3 less than current one 
    check = lambda new, prev: new - prev >= 1 and new - prev <= 3

    index = 0

    while index < len(data):
        diff = data[index] - prev
        differences.append(diff)
        prev = data[index]
        index += 1
    else:
        diff = device - prev
        differences.append(diff)
    
    return differences

differences = main(data)

if __name__ == "__main__":
    print(differences.count(1) * differences.count(3))
