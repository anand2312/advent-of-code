"""Advent of Code Day 7"""
from __future__ import annotations
from utils import get_data
from dataclasses import dataclass
import typing

raw_data = get_data("bags")
# data is now in the form of a list of strings, with each string being a bag rule


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
            children[unparsed_child[1:_bag_index].strip(".").strip()] = int(unparsed_child[0])
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


@dataclass(eq=True, frozen=True)
class Bag:
    name: str
    children: typing.Mapping[str, int]

    @staticmethod
    def from_string(key: str, all_values: dict) -> Bag:
        return all_values[key]

    def __hash__(self):
        return hash(self.name)


@dataclass(eq=True, frozen=True)
class Node:
    state: Bag
    parent: Node


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node: Node) -> None:
        self.frontier.append(node)

    def is_empty(self) -> bool:
        return len(self.frontier) == 0

    def remove(self) -> Node:
        if self.is_empty():
            raise Exception("Empty Stack")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

    def contains_node(self, node: Node) -> bool:
        return any([node.state == element.state for element in self.frontier])


def solve(data: list) -> int:
    # goes through the data using the DFS algorithm
    data = parse_all_rules(data)
    first_element = list(data.values())[0]
    start = Node(state=first_element, parent=None)

    goal_state = Bag.from_string("shiny gold", data)
    stack = StackFrontier()
    stack.add(start)

    explored_set = set()
    explored_count = 0
    parent_count = 0

    while True:
        if stack.is_empty():
            return parent_count

        node = stack.remove()
        explored_count += 1

        if node.state == goal_state:
            parent_nodes = []

            while node.parent is not None:
                parent_nodes.append(node)
                node = node.parent

            parent_count += len(parent_nodes)

        explored_set.add(node)

        if node.state.children is None:
            continue

        for bag in node.state.children.keys():    # node.state -> Bag object, now Bag.children is a dict, doing values makes it a list of child Bags
            bag = Bag.from_string(bag, data)
            as_node = Node(state=bag, parent=node)
            if not stack.contains_node(as_node):
                stack.add(as_node)


if __name__ == "__main__":
    raw_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split("\n")
    print(solve(raw_data))
    