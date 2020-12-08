"""Advent of Code Day 8"""
from utils import get_data

data = get_data("instructions")
# data is now in the form of a list of strings, with each string being an instruction

class Instruction:
    def __init__(self, action: str, arg: str):
        self.action = action
        self.arg = arg
        self.done = False

    def execute(self):
        if self.action in {"acc", "jmp"}:
            self.done = True
            return int(self.arg)
        else:
            self.done = True
            return 0


class Executor:
    def __init__(self):
        self.accumulator = 0

    def compile_instruction(self, command: str) -> Instruction:
        # misleading name?
        # just converts a string instruction into an object
        return Instruction(*command.split())

    def run(self, commands: list):
        # breaks at first instance where a command is repeated
        current_index = 0
        commands = list(map(self.compile_instruction, commands))
        while True:
            current_instruction = commands[current_index]
            if not current_instruction.done:
                if current_instruction.action == "acc":
                    self.accumulator += current_instruction.execute()
                    current_index += 1
                elif current_instruction.action == "jmp":
                    offset = current_instruction.execute()
                    current_index += offset
                    continue
                else:
                    current_index += 1
            else:
                print(self.accumulator)
                return self.accumulator


def main() -> None:
    loop = Executor()
    loop.run(data)

main()