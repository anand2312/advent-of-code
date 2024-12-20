"""Helper functions"""
import os
import pathlib
from itertools import islice
from typing import List

import requests
from dotenv import load_dotenv

load_dotenv(pathlib.Path(__file__).parent.parent.parent / ".env")


BASE_URL = "https://adventofcode.com/2024/day/{day}"
INPUT_URL = BASE_URL + "/input"
INPUT_DIR = pathlib.Path(__file__).parent.parent / "inputs"


def chunks(iterable, n):
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


class Puzzle:
    def __init__(self, day: int) -> None:
        self.day = day
        self._input_file = INPUT_DIR / f"day_{day:0>2}.txt"
        self._sample_file = INPUT_DIR / f"sample_{day:0>2}.txt"

        if self._input_file.exists():
            self.raw_content = self._input_file.read_text().strip()
        else:
            self.get_input_data()

    def sample_lines(self) -> List[str]:
        """Returns the sample input as a list of lines"""
        if not self._sample_file.exists():
            raise ValueError(f"Sample data not found for day: {self.day}")
        return self._sample_file.read_text().splitlines()

    def sample(self) -> str:
        """Returns the sample input, as is."""
        if not self._sample_file.exists():
            raise ValueError(f"Sample data not found for day: {self.day}")
        return self._sample_file.read_text()

    def intlines(self) -> List[int]:
        """Splits the raw content and converts each element to an integer"""
        return [int(i) for i in self.raw_content.split()]

    def lines(self) -> List[str]:
        """Returns the input as a list of lines"""
        return self.raw_content.splitlines()

    def get_input_data(self) -> None:
        """Make an HTTP request to AoC, fetch the input data and make a file."""
        session = os.environ.get("AOC_SESSION_COOKIE")
        if not session:
            raise ValueError("Session cookie not found")
        r = requests.get(INPUT_URL.format(day=self.day), cookies={"session": session})

        self.raw_content = r.text.strip()
        self._input_file.write_text(r.text)
