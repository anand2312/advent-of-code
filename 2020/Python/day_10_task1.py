"""Advent of Code Day 10"""
from utils import get_data

data = get_data("adapters")

def main(data: list) -> int:
    differences = []
    data = sorted(data)

    device = data[-1] + 3
    prev = 0

    # can only connect if the previous jolt is 1-3 less than current one 
    check = lambda new, prev: new - prev >= 1 and new - prev <= 3

    count = 0

    while count < len(data):
        diff = data[count] - prev
        differences.append(diff)
        prev = data[count]
        count += 1
    else:
        diff = device - prev
        differences.append(diff)
    
    return differences

differences = main(data)

if __name__ == "__main__":
    print(differences.count(1) * differences.count(3))