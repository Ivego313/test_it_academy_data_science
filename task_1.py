def get_unique_sorted_numbers(x: list[int]) -> list[int]:
    return list(sorted(set(x)))


numbers = [4, 2, 101, 2, 6, 7, 4, 5, 5, 6, 8, 8, 1, 4]
print(f"Input numbers: {numbers}")
print(f"Unique sorted numbers: {get_unique_sorted_numbers(numbers)}")
