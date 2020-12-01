"""Helper functions to handle data"""
import typing
import json

def get_data(key: str) -> typing.Any:
  with open("inputs.json", "r") as f:
    data = json.load(f)[key] 
  return data