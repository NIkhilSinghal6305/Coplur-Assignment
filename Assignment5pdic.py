# 1) Write a Python program to repeat a tuple three times using the * operator.

t = (1, 2, 3)

result = t * 3

print("Q1 Output:", result)


# 2) Write a Python program to join three separate tuples into one new tuple using the + operator.

t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)

joined_tuple = t1 + t2 + t3

print("Q2 Output:", joined_tuple)


# 3) Write a Python program to check whether a specific element exists inside a tuple using the in keyword.

t = (10, 20, 30, 40)

element = 30

if element in t:
    print("Q3 Output: Element found")
else:
    print("Q3 Output: Element not found")


# 4) Write a Python program to calculate the total, highest value, and lowest value from a tuple of integers
# without using the built-in sum(), max(), and min() functions.

numbers = (12, 45, 7, 23, 89, 34)

total = 0
highest = numbers[0]
lowest = numbers[0]

for num in numbers:
    total += num

    if num > highest:
        highest = num

    if num < lowest:
        lowest = num

print("Q4 Output:")
print("Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)


# 5) Write a Python program to filter a tuple.
# n = (3, 14, 7, 22, 9, 41, 18, 5), keep only values greater than 10.

n = (3, 14, 7, 22, 9, 41, 18, 5)

filtered = ()

for num in n:
    if num > 10:
        filtered += (num,)

print("Q5 Output:", filtered)


# 6) Write a Python program to determine how many elements are in a set
# without using the built-in len() function.

s = {"cat", "dog", "bird", "fish"}

count = 0

for item in s:
    count += 1

print("Q6 Output:", count)


# 7) Write a Python program to combine two sets into one,
# containing all unique elements from both sets.

s1 = {1, 2, 3}
s2 = {3, 4, 5}

union_set = s1 | s2

print("Q7 Output:", union_set)


# 8) Write a Python program to find all elements that are common to both sets.

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

common_elements = s1 & s2

print("Q8 Output:", common_elements)


# 9) Write a Python program to find all elements that are in either set
# but not in both sets (symmetric difference).

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

symmetric_difference = s1 ^ s2

print("Q9 Output:", symmetric_difference)