#26-06-26
# Working with Lambda Functions

# -----------------------------------------
# Task 1: Sort a list of dictionaries
# -----------------------------------------

students = [
    {"name": "Ravi", "marks": 85},
    {"name": "Sita", "marks": 92},
    {"name": "Kiran", "marks": 78},
    {"name": "Anu", "marks": 88}
]

# Sort dictionaries based on marks
sorted_students = sorted(students, key=lambda student: student["marks"])

print("Task 1: Students sorted by marks")
for student in sorted_students:
    print(student)


# -----------------------------------------
# Task 2: Filter odd numbers
# -----------------------------------------

numbers = [10, 15, 22, 31, 40, 45, 52, 63]

# Use lambda to check whether a number is odd
odd_numbers = list(filter(lambda number: number % 2 != 0, numbers))

print("\nTask 2: Odd numbers")
print(odd_numbers)


# -----------------------------------------
# Task 3: Calculate square of each number
# -----------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

# Use lambda with map to calculate squares
squared_numbers = list(map(lambda number: number ** 2, numbers))

print("\nTask 3: Squares of numbers")
print(squared_numbers)