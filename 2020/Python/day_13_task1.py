"""Advent of Code Day 13"""
from utils import get_data

data = get_data("bus shuttle")

minimum = data["minimum timestamp"]
ids = data["bus ids"]

def main() -> None:
    results = []
    for i in filter(lambda x: isinstance(x, int), ids):
        multiply = 1
        val = 1
        while val < minimum:
            val = i * multiply
            multiply += 1
        else:
            results.append({"id": i, "value": val})
    key = lambda x: x['value']
    best = min(results, key=key)
    print(best['id'] * (best['value'] - minimum))

main()
