"""Advent of Code Day 7"""
from utils import get_data
from dataclasses import dataclass
import typing
import pprint

raw_data = get_data("bags")
# data is now in the form of a list of strings, with each string being a bag rule

@dataclass
class Bag:
    name: str
    children: typing.Mapping[str, int]

    def get_from_string(self, key: str, all_values: dict) -> "Bag":
        return all_values[key]


def parse_rule(rule: str) -> typing.Mapping[str, Bag]:
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
            children[unparsed_child[1:_bag_index].strip(".").strip()] = int(unparsed_child[0])
        except ValueError:
            # a ValueError is raised when 'no bags' occurs. in this case, keep the children part as None
            children = None

    parsed["children"] = children
    bag_obj = Bag(**parsed)

    return {parsed['name']: bag_obj}

def parse_all_rules(data: list) -> dict:
    parsed = {}

    for rule in data:
        parsed_rule = parse_rule(rule)
        parsed = {**parsed, **parsed_rule}

    return parsed

parsed_data = parse_all_rules(raw_data)



        





        

    