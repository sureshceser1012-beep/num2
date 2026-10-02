import numpy as np


def create_vector():
    return np.arange(1, 11)


def scale_and_shift(arr, scale, shift):
    return arr * scale + shift


def array_statistics(arr):
    mean = np.mean(arr)
    median = np.median(arr)
    std = np.std(arr)

    return mean, median, std


# Testing

vector = create_vector()
print("Vector:", vector)

arr = np.array([1, 2, 3, 4, 5])
print("Scaled and shifted:", scale_and_shift(arr, 2, 10))

print("Statistics:", array_statistics(arr))