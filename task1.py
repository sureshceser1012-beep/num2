def unique_words(text: str) -> set:
    words = text.lower().split()
    return {word.strip(".,!?;:'\"()[]{}") for word in words}


def merge_inventories(a: dict, b: dict) -> dict:
    result = a.copy()

    for item, quantity in b.items():
        if item in result:
            result[item] += quantity
        else:
            result[item] = quantity

    return result


def common_elements(map1: dict, map2: dict) -> set:
    return set(map1.keys()) & set(map2.keys())


# Test cases

text = "Python is easy, Python is powerful!"
print(unique_words(text))

inventory1 = {"apple": 10, "banana": 5}
inventory2 = {"banana": 3, "orange": 7}
print(merge_inventories(inventory1, inventory2))

map1 = {"a": 1, "b": 2, "c": 3}
map2 = {"b": 5, "c": 6, "d": 7}
print(common_elements(map1, map2))