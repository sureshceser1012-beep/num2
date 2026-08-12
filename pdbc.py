import sqlite3

# PDBC Connection
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

print("PDBC connection established successfully.")

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

# Insert at least 5 records
students = [
    ("Ravi", 20, "Python"),
    ("Sita", 21, "Java"),
    ("Kiran", 22, "Python"),
    ("Anu", 20, "SQL"),
    ("Rahul", 23, "Python")
]

cursor.executemany("""
INSERT INTO student (name, age, course)
VALUES (?, ?, ?)
""", students)

connection.commit()

print("\n5 records inserted successfully.")

# Retrieve all records
print("\nAll Student Records:")
cursor.execute("SELECT * FROM student")

rows = cursor.fetchall()

for row in rows:
    print(row)

# Update records
# Change course to 'Advanced Python' for students whose course is Python
cursor.execute("""
UPDATE student
SET course = 'Advanced Python'
WHERE course = 'Python'
""")

connection.commit()

print("\nRecords updated successfully.")

# Display updated records
print("\nUpdated Student Records:")
cursor.execute("SELECT * FROM student")

rows = cursor.fetchall()

for row in rows:
    print(row)

# Close connection
cursor.close()
connection.close()

print("\nPDBC connection closed.")