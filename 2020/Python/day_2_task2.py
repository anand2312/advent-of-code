from day_2_task1 import parsed_data, ParsedElement

# in this case `low` and `high` are positions in the string
# the condition now is char in `low` XOR char in `high`

def check(element: ParsedElement) -> bool:
    results = [element.char == element.pw[element.low-1], element.char == element.pw[element.high-1]]
    return results[0] ^ results[1]

print(len(list(filter(check, parsed_data))))