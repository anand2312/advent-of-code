"""Advent of Code Day 6"""
from utils import get_data

raw_data = get_data("customs")

def count_per_group(replies: str) -> int:
    # this time, return count of questions EVERYONE answered yes to
    people = []
    for person in replies.split("\n"):
        people.append(set(person))
    return len(people[0].intersection(*people[1:]))

def main() -> None:
    print(sum(count_per_group(i) for i in raw_data))
