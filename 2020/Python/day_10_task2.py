"""Advent of Code Day 10"""
from utils import get_data
import itertools
import typing

data = get_data("adapters")

def find_combinations(data: list) -> set:
    data = sorted(data)
    adapter = data[-1] + 3
    data.extend([0, adapter])
    data = sorted(data)

    def is_valid_combination(combination: typing.Sequence) -> bool:
        combination = sorted(combination)

        nonlocal adapter
        if not combination[0] == 0 and combination[-1] == adapter:
            return False
        
        prev = combination[0]
        for i in combination[1:]:
            if not (i - prev >= 1 and i - prev <= 3):
                return False
            else:
                prev = i
        else:
            return True

    valid = set()

    most = len(data)
    least = len(data) // 3
    
    for i in range(least, most + 1):
        all_combinations = itertools.combinations(data, i)
        valid.update(all_combinations)

    valid = filter(is_valid_combination, valid)
    
    return valid

def main(data: list) -> int:
    return len(find_combinations(data))

if __name__ == "__main__":
    print(main(data))



    
