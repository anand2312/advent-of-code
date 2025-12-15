from typing import Literal
from operator import add, mul

from helpers import Puzzle
import polars as pl

puzzle = Puzzle(day=6)


def to_df(lines: list[str]) -> tuple[pl.DataFrame, list[Literal["+", "*"]]]:
    x = [list(line) for line in lines]
    df = pl.DataFrame(x[:-1])
    return df, [i for i in x[-1] if not i.isspace()]  # type: ignore

def main(lines: list[str]) -> int:
    df, ops = to_df(lines)
    df = df.transpose().select(pl.all().str.join())
    op_idx = 0
    op_map = {
        "*": mul,
        "+": add
    }
    results: list[int] = [1 if ops[0] == "*" else 0]

    for col in df.columns:
        if df.select(pl.col(col).str.strip_chars() == "").item():
            op_idx += 1
            # create a new "field" in the results list 
            # for the next calculation
            results.append(1 if ops[op_idx] == "*" else 0)
            continue
        
        results[op_idx] = op_map[ops[op_idx]](results[op_idx], df.select(pl.col(col).str.strip_chars().cast(pl.Int64)).item())

    return sum(results)


if __name__ == "__main__":
    # print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))