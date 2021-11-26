"""Advent of Code Day 7"""
from __future__ import annotations

import typing
from utils import get_data
from dataclasses import dataclass


raw_data = get_data("bags")
# data is now in the form of a list of strings, with each string being a bag rule


@dataclass(eq=True, frozen=True)
class Bag:
    name: str
    children: typing.Mapping[str, int]

    @staticmethod
    def from_string(key: str, all_values: dict) -> Bag:
        return all_values[key]

    def __hash__(self):
        return hash(self.name)


def parse_rule(rule: str) -> typing.Mapping[str, Bag]:
    # parse a single rule string and return a dictionary, of the string of the color mapped to the Bag object
    parsed = dict()
    children = dict()

    # first split gets the name
    name, rest = rule.split(" bags contain ")
    parsed["name"] = name

    # next split gets the child bags and their counts

    children_unparsed = rest.split(", ")

    for unparsed_child in children_unparsed:
        # the word 'bags' isn't needed in the color name
        try:
            unparsed_child = unparsed_child.strip()
            _bag_index = unparsed_child.find("bag")
            children[unparsed_child[1:_bag_index].strip(".").strip()] = int(unparsed_child[0]) # type: ignore
        except ValueError:
            # a ValueError is raised when 'no bags' occurs. in this case, keep the children part as None
            children = None

    parsed["children"] = children
    bag_obj = Bag(**parsed)

    return {parsed['name']: bag_obj}


def parse_all_rules(data: list) -> dict:
    # call parse_rule over and over to parse all the rules, and return a dictionary with the color: Bag for all of them
    parsed = {}

    for rule in data:
        parsed_rule = parse_rule(rule)
        parsed = {**parsed, **parsed_rule}

    return parsed


def reach_shiny_gold(bag: Bag, all_bags: dict[str, Bag]) -> bool:
    # go through the children to see if it eventually reaches a shiny gold
    if bag.children is None:
        # reached lowest case without reaching shiny gold
        return False
    if 'shiny gold' in bag.children:
        return True
    else:
        results = []
        for child_name in bag.children:
            child_bag = all_bags[child_name]
            results.append(reach_shiny_gold(child_bag, all_bags))
        return any(results)


if __name__ == "__main__":
    bags = parse_all_rules(raw_data)

    count = 0

    for i in bags.values():
        res = reach_shiny_gold(i, bags)
        if res is True:
            count += 1
        elif res is None:
            print("BROO!!!", i)
    
    print(count)

    