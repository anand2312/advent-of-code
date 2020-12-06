from utils import get_data

raw_data = get_data("customs")

def count_per_group(replies: str) -> int:
    counts = set(replies)
    if "\n" in replies:
        return len(counts) - 1
    else:
        return len(counts)

def main() -> None:
    print(sum(count_per_group(i) for i in raw_data))

