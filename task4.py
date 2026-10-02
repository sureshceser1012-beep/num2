import numpy as np


def create_matrix(rows: int, cols: int) -> np.ndarray:
    return np.arange(1, rows * cols + 1).reshape(rows, cols)


def scale_and_offset(arr: np.ndarray, scale: float, offset: float) -> np.ndarray:
    return arr * scale + offset


def column_stats(arr: np.ndarray) -> dict:
    return {
        "mean": np.mean(arr, axis=0),
        "median": np.median(arr, axis=0),
        "std": np.std(arr, axis=0)
    }


# Test cases

matrix = create_matrix(2, 3)
print(matrix)

arr = np.array([1, 2, 3, 4])
print(scale_and_offset(arr, 2, 5))

data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(column_stats(data))