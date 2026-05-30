import numpy as np
from statistics import mode

# 1. Combining a 1D and a 2D NumPy Array
arr1d = np.array([1, 2, 3])

arr2d = np.array([
    [4, 5, 6],
    [7, 8, 9]
])

combined = np.vstack((arr1d, arr2d))

print("Combined Array:")
print(combined)

# 2. Flatten a 2D array into a 1D array
flat = arr2d.flatten()

print("\nFlattened Array:")
print(flat)

# 3. Reverse a NumPy Array
arr = np.array([10, 20, 30, 40, 50])

print("\nReversed Array:")
print(arr[::-1])

# 4. Array Operations
array = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nMaximum Value:", np.max(array))
print("Minimum Value:", np.min(array))

rows, cols = array.shape
print("Rows:", rows)
print("Columns:", cols)

print("\nWhole Array:")
print(array)

print("Specific Element [1,2]:", array[1, 2])

# Sum using for loop
total = 0
for row in array:
    for element in row:
        total += element

print("Sum using for loop:", total)

# Arithmetic Operations
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 5. Iterate a 3D Array
arr3d = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("\n3D Array Iteration using Nested Loops:")
for x in arr3d:
    for y in x:
        for z in y:
            print(z, end=" ")

print("\n\n3D Array Iteration using nditer:")
for i in np.nditer(arr3d):
    print(i, end=" ")

# 6. Average, Mean, Median, Mode of Two 2D Arrays
arrA = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arrB = np.array([
    [6, 5, 4],
    [3, 2, 1]
])

avg_array = (arrA + arrB) / 2

print("\n\nAverage Array:")
print(avg_array)

combined_elements = np.concatenate((arrA.flatten(), arrB.flatten()))

print("\nMean:", np.mean(combined_elements))
print("Median:", np.median(combined_elements))
print("Mode:", mode(combined_elements))