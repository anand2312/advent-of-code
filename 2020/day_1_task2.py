"""Advent of Code Day 1"""
from utils import get_data

report = get_data('report')
# wow i don't know how to make this more efficient

for i in report:
  for j in report:
    if (i + j) < 2020:
      if (k := 2020 - (i + j)) in report:
        print(i*j*k)