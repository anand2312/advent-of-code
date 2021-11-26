"""Advent of Code Day 13"""
from utils import get_data


data = get_data("bus shuttle")

minimum = data["minimum timestamp"]
ids = data["bus ids"]

"""
naive implementation:
this won't get to the answer but it works for smaller test cases

first = ids[0]
multiplier = 1
largest = max([i for i in ids if isinstance(i, int)])

while multiplier * first <= largest:
    multiplier += 1

# answer t SHOULD be a multiple of first
# then match the next ID with it's offset
# if it doesn't match, multiply the guess again to get a bigger guess

while True:
    guess = first * multiplier

    for i, bus_id in enumerate(ids):
        if bus_id == "x":
            continue
        if (guess + i) % bus_id != 0:
            # one of the bus IDs don't occur at the required offset
            # increase multiplier and try all IDs again
            multiplier += 1
            break
    else:
        print(guess)
        break
"""