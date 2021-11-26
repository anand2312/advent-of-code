"""Advent of Code Day 7"""
from typing import Dict

from day_07_task1 import Bag, parse_all_rules
from utils import get_data


raw_data = get_data("bags") # data is now in the form of a list of strings, with each string being a bag rule
bags = parse_all_rules(raw_data)

# Bag -> name: str, the color of the bag and children: dict[str, int], with color name: count
# problem is to count the total number of bags inside our shiny gold bag

shiny_gold = bags["shiny gold"]


def count_children(bag: Bag, count: int, all_bags: Dict[str, Bag]) -> int:
    # recursively count the number of child bags in the specified bag
    if bag.children is None:
        return count
    
    for child_color, child_count in bag.children.items():
        child_bag = all_bags[child_color]
        count += child_count
        count += child_count * count_children(child_bag, 0, all_bags)
    
    return count


print(count_children(shiny_gold, 0, bags))
