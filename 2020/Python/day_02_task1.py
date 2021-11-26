"""Advent of Code Day 2"""
from utils import get_data
from collections import namedtuple

# data in inputs.json is now a list, with string elements
# each string being in the rule : password form

raw_data = get_data('passwords')
ParsedElement = namedtuple('ParsedElement', 'low high char pw')

def check(element: ParsedElement) -> bool:
    """Returns True if the password fits the rule."""
    count = element.pw.count(element.char)
    return (count >= element.low) and (count <= element.high)

def more_parse(value: str) -> ParsedElement:
    """Takes raw data and organizes it into the namedtuple for easy access."""
    values = value.split(': ')
    pw = values[1]
    range_, char = values[0].split()
    low, high = map(int, range_.split("-"))
    return ParsedElement(low, high, char, pw)

parsed_data = map(more_parse, raw_data)

if __name__ == "__main__":
    print(len(list(filter(check, parsed_data))))
