"""
Numpy tasks

Run with: python numpy_tasks.py
"""

import numpy as np
from datetime import date, timedelta

np.set_printoptions(precision=2, suppress=True)


# ---------------------------------------------------------------------------
# Task 1: Create a vector with values ranging from 10 to 49.
#         Reverse a vector (first element becomes last)
# ---------------------------------------------------------------------------
vec = np.arange(10, 50)
print("1. Vector:", vec)
reversed_vec = vec[::-1]
print("   Reversed:", reversed_vec, "\n")


# ---------------------------------------------------------------------------
# Task 2: Create a 5x5 array with random values and find the
#         minimum and maximum values
# ---------------------------------------------------------------------------
arr5x5 = np.random.random((5, 5))
print("2. 5x5 random array:\n", arr5x5)
print("   Min:", arr5x5.min(), "| Max:", arr5x5.max(), "\n")


# ---------------------------------------------------------------------------
# Task 3: Normalize a 5x5 random matrix
# ---------------------------------------------------------------------------
mat = np.random.random((5, 5))
normalized = (mat - mat.min()) / (mat.max() - mat.min())
print("3. Original matrix:\n", mat)
print("   Normalized (0-1 range):\n", normalized, "\n")


# ---------------------------------------------------------------------------
# Task 4: Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
# ---------------------------------------------------------------------------
m1 = np.random.randint(1, 10, (5, 3))
m2 = np.random.randint(1, 10, (3, 2))
product = m1 @ m2  # same as np.dot(m1, m2)
print("4. 5x3 matrix:\n", m1)
print("   3x2 matrix:\n", m2)
print("   Product (5x2):\n", product, "\n")


# ---------------------------------------------------------------------------
# Task 5: How to get the dates of yesterday, today and tomorrow?
# ---------------------------------------------------------------------------
today_np = np.datetime64("today")
yesterday_np = today_np - np.timedelta64(1, "D")
tomorrow_np = today_np + np.timedelta64(1, "D")
print("5. Yesterday:", yesterday_np, "| Today:", today_np, "| Tomorrow:", tomorrow_np, "\n")


# ---------------------------------------------------------------------------
# Task 6: Extract the integer part of a random array using 5 different methods
# ---------------------------------------------------------------------------
rand_arr = np.random.uniform(0, 10, 6)
print("6. Random array:", rand_arr)
print("   Method 1 (np.floor):     ", np.floor(rand_arr))
print("   Method 2 (astype int):   ", rand_arr.astype(int))
print("   Method 3 (np.trunc):     ", np.trunc(rand_arr))
print("   Method 4 (subtract frac):", rand_arr - rand_arr % 1)
print("   Method 5 (np.int_):      ", np.int_(rand_arr), "\n")


# ---------------------------------------------------------------------------
# Task 7: Create a structured array representing a position (x,y)
#         and a color (r,g,b)
# ---------------------------------------------------------------------------
dtype = [("position", [("x", float), ("y", float)]),
         ("color", [("r", int), ("g", int), ("b", int)])]
structured = np.zeros(3, dtype=dtype)
structured["position"]["x"] = [1.0, 2.5, 3.2]
structured["position"]["y"] = [4.0, 5.5, 6.1]
structured["color"]["r"] = [255, 0, 100]
structured["color"]["g"] = [0, 255, 150]
structured["color"]["b"] = [0, 0, 200]
print("7. Structured array:\n", structured, "\n")


# ---------------------------------------------------------------------------
# Task 8: Consider a generator function that generates 10 integers
#         and use it to build an array
# ---------------------------------------------------------------------------
def generate_integers():
    for i in range(10):
        yield i

gen_array = np.fromiter(generate_integers(), dtype=int)
print("8. Array from generator:", gen_array, "\n")


# ---------------------------------------------------------------------------
# Task 9: Consider two random array A and B, check if they are equal
# ---------------------------------------------------------------------------
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = np.array_equal(A, B)
print("9. A:", A, "| B:", B, "| Equal:", equal, "\n")


# ---------------------------------------------------------------------------
# Task 10: Consider a random vector with shape (100,2) representing
#          coordinates, find point by point distances
# ---------------------------------------------------------------------------
coords = np.random.random((100, 2))
# distance between every pair of points -> 100x100 distance matrix
diff = coords[:, np.newaxis, :] - coords[np.newaxis, :, :]
distances = np.sqrt((diff ** 2).sum(axis=-1))
print("10. Coordinates shape:", coords.shape)
print("    Distance matrix shape:", distances.shape)
print("    Distance between point 0 and point 1:", distances[0, 1], "\n")


# ---------------------------------------------------------------------------
# Task 11: Subtract the mean of each row of a matrix
# ---------------------------------------------------------------------------
matrix = np.random.randint(1, 10, (4, 4)).astype(float)
row_means = matrix.mean(axis=1, keepdims=True)
centered = matrix - row_means
print("11. Original matrix:\n", matrix)
print("    Row means:", row_means.ravel())
print("    After subtracting row mean:\n", centered, "\n")


# ---------------------------------------------------------------------------
# Task 12: How do I sort an array by the nth column?
# ---------------------------------------------------------------------------
to_sort = np.random.randint(0, 10, (5, 3))
n = 1  # sort by column index 1
sorted_by_col = to_sort[to_sort[:, n].argsort()]
print("12. Original array:\n", to_sort)
print(f"    Sorted by column {n}:\n", sorted_by_col, "\n")


# ---------------------------------------------------------------------------
# Task 13: Compute a matrix rank
# ---------------------------------------------------------------------------
rank_matrix = np.random.randint(0, 10, (4, 4))
rank = np.linalg.matrix_rank(rank_matrix)
print("13. Matrix:\n", rank_matrix)
print("    Rank:", rank, "\n")


# ---------------------------------------------------------------------------
# Task 14: Consider a 16x16 array, how to get the block-sum (block size is 4x4)
# ---------------------------------------------------------------------------
big_arr = np.ones((16, 16), dtype=int)
block_size = 4
block_sum = big_arr.reshape(16 // block_size, block_size, 16 // block_size, block_size).sum(axis=(1, 3))
print("14. 16x16 array summed into 4x4 blocks:\n", block_sum)