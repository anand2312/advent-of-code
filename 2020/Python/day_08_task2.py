"""Advent of Code Day 8"""
from copy import deepcopy
from typing import List

from utils import get_data
from day_08_task1 import Instruction, Executor


data = get_data("instructions")


class WorkingExecutor(Executor):
    # this executor should try to swap a nop / jmp to get it to
    # terminate normally
    def __init__(self, raw_commands: List[str]) -> None:
        super().__init__()
        self.commands: List[Instruction] = list(map(self.compile_instruction, raw_commands))

    @staticmethod
    def run(cmds: List[Instruction]) -> int:
        # runs the commands
        # if it results in an infinite loop, returns -1
        # else returns the accumulator
        accumulator = 0 
        current_index = 0

        while True:
            if current_index >= len(cmds):
                return accumulator

            current_instruction = cmds[current_index]
            if not current_instruction.done:
                if current_instruction.action == "acc":
                    accumulator += current_instruction.execute()
                    current_index += 1
                elif current_instruction.action == "jmp":
                    offset = current_instruction.execute()
                    current_index += offset
                    continue
                else:
                    current_index += 1
            else:
                for i in cmds:
                    i.done = False
                return -1

    def run_until_ends(self) -> int:  # type: ignore
        # run like old executor
        # while swapping a nop for jmp and vice versa
        # if current index reaches len(cmds), break
        for i, instruction in enumerate(self.commands):
            if instruction.action == "jmp":
                swapped = Instruction(action="nop", arg=instruction.arg)
            elif instruction.action == "nop":
                swapped = Instruction(action="jmp", arg=instruction.arg)
            else:
                continue

            cmds_copy = deepcopy(self.commands)
            cmds_copy[i] = swapped

            res = WorkingExecutor.run(cmds_copy)

            if res == -1:
                continue
            else:
                return res


if __name__ == "__main__":
    loop = WorkingExecutor(data)
    print(loop.run_until_ends())
