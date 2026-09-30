# List Methods Revision Assignment


# 1. Add Elements
def add_elements(base_list, elements):
    result = base_list.copy()
    result.extend(elements)
    return result


# 2. Remove First Occurrence
def remove_first_occurrence(data_list, value):
    if value in data_list:
        data_list.remove(value)
    return data_list


# 3. Filter and Sort
def filter_and_sort(numbers):
    result = [number for number in numbers if number % 2 == 0]
    result.sort(reverse=True)
    return result


# Testing

print(add_elements([1, 2, 3], [4, 5]))

data = [10, 20, 30, 20, 40]
print(remove_first_occurrence(data, 20))

print(filter_and_sort([5, 8, 2, 9, 6, 4, 1]))