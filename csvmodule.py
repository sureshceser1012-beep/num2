import csv
import random

# --------------------------------------------------
# Task 1: Read example.csv and print first 5 rows
# --------------------------------------------------

print("TASK 1: First 5 Rows from example.csv")

try:
    with open("example.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for i, row in enumerate(reader):
            print(row)

            if i == 4:
                break

except FileNotFoundError:
    print("example.csv not found.")


# --------------------------------------------------
# Task 2: Generate output.csv with 10 random users
# --------------------------------------------------

names = [
    "suresh", "priya", "madhura", "jhon", "Rahul",
    "suresh roy", "Arjun", "Sneha", "Vijay", "Kavya"
]

cities = [
    "Hyderabad", "Chennai", "Bangalore",
    "Mumbai", "Delhi", "Pune"
]

with open("output.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(10):
        writer.writerow({
            "name": random.choice(names),
            "age": random.randint(18, 35),
            "city": random.choice(cities)
        })

print("\noutput.csv created successfully with 10 records.")


# --------------------------------------------------
# Task 3: Add id column to example.csv
# --------------------------------------------------

try:
    with open("example.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    fieldnames = ["id"] + reader.fieldnames

    with open("modified_example.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for unique_id, row in enumerate(rows, start=1):
            row["id"] = unique_id
            writer.writerow(row)

    print("modified_example.csv created successfully.")

except FileNotFoundError:
    print("example.csv not found. Task 3 cannot be completed.")