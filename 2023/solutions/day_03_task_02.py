import operator
from helpers import Puzzle
from day_03_task_01 import nums_positions, is_neighbour


def main(lines: list[str]) -> int:
    total = 0
    nums, _ = nums_positions(lines)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != "*":
                continue
            adj_nums = []
            # i could just search for numbers in the neighbourhood of this point
            # but i'm too lazy. going through all the numbers will be slower
            # but who cares lmao
            for num_bounds in nums:
                if len(adj_nums) > 2:
                    break
                if is_neighbour((x, y), num_bounds):
                    adj_nums.append(nums[num_bounds])
            if len(adj_nums) == 2:
                total += operator.mul(*adj_nums)
    return total


if __name__ == "__main__":
    puzzle = Puzzle(day=3)
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))
