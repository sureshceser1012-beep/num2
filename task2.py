def filter_even_numbers(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]


def tuple_to_list(pair: tuple[int, int]) -> list[int]:
    return list(pair)


def merge_and_sort(seq1: list[int], seq2: tuple[int, ...]) -> list[int]:
    return sorted(set(seq1 + list(seq2)))


# Test cases

numbers = [1, 2, 3, 4, 5, 6]
print(filter_even_numbers(numbers))

pair = (10, 20)
print(tuple_to_list(pair))

seq1 = [5, 2, 8, 2]
seq2 = (3, 8, 1, 5)
print(merge_and_sort(seq1, seq2))