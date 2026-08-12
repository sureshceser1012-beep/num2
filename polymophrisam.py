import mysql.connector

# PDBC Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = con.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS college")
cursor.execute("USE college")

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    rollno INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
)
""")

# Multiple records using loop
n = int(input("Enter number of records: "))

for i in range(n):
    print("\nEnter details for record", i + 1)

    rollno = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    query = """
    INSERT INTO student (rollno, name, age, course)
    VALUES (%s, %s, %s, %s)
    """

    values = (rollno, name, age, course)

    cursor.execute(query, values)

con.commit()

print("\nAll records inserted successfully!")

cursor.close()
con.close()