import re


# --------------------------------------------------
# Task 1: Pattern Matching
# --------------------------------------------------

def check_pattern(text):
    pattern = r"(\b[\w.-]+@[\w.-]+\.\w+\b)|(\(\d{3}\) \d{3}-\d{4})"

    if re.search(pattern, text):
        return True
    return False


test_strings = [
    "Contact me at john@gmail.com",
    "My phone number is (123) 456-7890",
    "Hello, how are you?",
    "Email: student@example.com"
]

print("TASK 1: Pattern Matching")

for text in test_strings:
    if check_pattern(text):
        print(text, "-> Pattern Found")
    else:
        print(text, "-> Pattern Not Found")


# --------------------------------------------------
# Task 2: String Searching
# --------------------------------------------------

text = """Python is easy to learn.
Python is widely used in data science.
Regular expressions are useful in Python.
Python makes text processing easier."""

search_word = "Python"

print("\nTASK 2: String Searching")

for line_number, line in enumerate(text.splitlines(), start=1):
    for match in re.finditer(search_word, line):
        print(
            "Word:", search_word,
            "| Line:", line_number,
            "| Character Position:", match.start()
        )


# --------------------------------------------------
# Task 3: Data Extraction from Text File
# --------------------------------------------------

file_name = "sample.txt"

# Create sample text file
with open(file_name, "w") as file:
    file.write("""
Visit https://www.google.com for more information.
Our website is https://www.example.com.
The meeting date is 20-07-2026.
Another event is scheduled for 15-08-2026.
""")

# Read the text file
with open(file_name, "r") as file:
    file_data = file.read()

# Extract URLs
url_pattern = r"https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

urls = re.findall(url_pattern, file_data)

# Extract dates
date_pattern = r"\b\d{2}-\d{2}-\d{4}\b"

dates = re.findall(date_pattern, file_data)

print("\nTASK 3: Data Extraction")

print("URLs:")
for url in urls:
    print(url)

print("\nDates:")
for date in dates:
    print(date)