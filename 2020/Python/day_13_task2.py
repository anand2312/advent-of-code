"""Advent of Code Day 13"""
from utils import get_data


data = get_data("bus shuttle")
ids = data["bus ids"]

# Chinese Remainder Theorem: https://www.youtube.com/watch?v=zIFehsBHB8o
# x === b (mod n),
# which means that when x is divided by n, the remainder is b
# CRT works on a series of such moduli where the n's are all mutually prime
# that is, they have no common factors except 1
# For such a series of moduli,
# x === b1 (mod n1)
# x === b2 (mod n2)
# ...
# x === bi (mod ni),
# and where Ni = N / ni, where N = n1 * n2 * n3 ... * ni (i.e Ni is product of all n except for ni)
# xi is inverse of corresponding Ni, calculated as shown https://youtu.be/zIFehsBHB8o?t=496 here.
# The number we need (x) is equal to sum of bi * Ni * xi

def inverse(x: int) -> int:
    # inverse as shown https://youtu.be/zIFehsBHB8o?t=496
    

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