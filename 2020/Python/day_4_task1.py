"""Advent of Code Day 4"""
from utils import get_data
from dataclasses import dataclass
import typing

raw_data = get_data("passports")
# the data is now in the form of a list of strings
# with each string being all of a passport's data

@dataclass
class Passport:
    """A dataclass that will accept all the fields for a passport.
    Raises error if any field except cid is missing."""
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: typing.Optional[str] = None

def parse_passport(raw: str) -> dict:
    d = {}
    for element in raw.split():   # split with no parameter splits at _every_ whitespace
        key, value = element.split(":")
        d[key] = value
    return d

def main() -> None:
    count = 0
    for raw_string in raw_data:
        try:
            _ = Passport(**parse_passport(raw_string))
            count += 1
        except TypeError:
            continue
    print(count)
