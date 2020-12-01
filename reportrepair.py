"""Advent of Code Day 1"""
import json

with open("inputs.json", "r") as f:
  report = json.load(f)['report']

for i in report:
    if (j := 2020 - i) in report:
        print(i * j)