"""Helper functions to handle data. Run files at root directory level."""
import typing
import json

def get_data(key: str) -> typing.Any:
  with open("2020/inputs.json", "r") as f:
    data = json.load(f)[key] 
  return data