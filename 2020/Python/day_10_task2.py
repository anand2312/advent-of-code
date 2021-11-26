"""Advent of Code Day 10"""
from typing import List
from utils import get_data

data = get_data("adapters")


def total_combinations(adaptors: List[int]) -> int:
    # The ways you can reach any "node" is with the sum of the ways you can reach its direct parents and only its direct parents
    adaptors = [0] + sorted(adaptors)
    path_counts = {adaptors[0]: 1}

    for i in adaptors[1:]:
        path_counts[i] = sum(path_counts.get(i - j, 0) for j in range(1, 4))

    return path_counts.popitem()[1]


if __name__ == "__main__":
    print(total_combinations(data))