# Set and Dictionary Revision Assignment


# 1. Unique Elements Extractor
def unique_items(iterable):
    return set(iterable)


# 2. Common Keys Merger
def merge_common_keys(dict_a, dict_b):
    result = {}

    for key in dict_a:
        if key in dict_b:
            result[key] = [dict_a[key], dict_b[key]]

    return result


# 3. Frequency Counter
def word_frequencies(text):
    words = text.lower().split()
    unique_words = set(words)

    result = {}

    for word in unique_words:
        result[word] = words.count(word)

    return result


# Testing


# Task 1
numbers = [1, 2, 2, 3, 4, 4, 5]
print("Unique Items:", unique_items(numbers))


# Task 2
dict_a = {
    "name": "Suresh",
    "age": 25,
    "city": "Hyderabad"
}

dict_b = {
    "age": 26,
    "city": "Bangalore",
    "course": "Python"
}

print("Common Keys:", merge_common_keys(dict_a, dict_b))


# Task 3
text = "Python is easy Python is powerful"
print("Word Frequencies:", word_frequencies(text))