from helpers import Puzzle
from day_04_task_01 import check_if_win, calculate_score, parse_input


puzzle = Puzzle(day=4)


def main() -> int:
    nums, boards, positions = parse_input()
    nums = iter(nums)

    while len(boards) > 1:
        # keep going through all boards
        # pop them from the list when they win
        current_num = next(nums)
        pos = positions[current_num]
        pos.marked = True

        # make a new list of boards, that haven't won yet
        boards = [board for board in boards if not check_if_win(board)]
    else:
        # only one board left
        # keep going till this board reaches a win state
        for num in nums:
            pos = positions[num]
            pos.marked = True

            if check_if_win(boards[0]):
                return calculate_score(boards[0], num)
        else:
            # fail case, only to appease type checker
            return -1


if __name__ == "__main__":
    print(main())
