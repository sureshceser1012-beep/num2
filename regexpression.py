import re

# --------------------------------------------------
# 1. Match strings containing a, b, or c
# --------------------------------------------------

pattern1 = r"[abc]"

strings = [
    "Apple",
    "Hello",
    "Python",
    "DOG",
    "Banana"
]

print("1. Strings containing a, b, or c:")

for text in strings:
    if re.search(pattern1, text, re.IGNORECASE):
        print(text, "-> Match")
    else:
        print(text, "-> No Match")


# --------------------------------------------------
# 2. Validate dates in dd-mm-yyyy format
# --------------------------------------------------

pattern2 = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"

dates = [
    "01-01-2022",
    "15-08-2026",
    "31-12-2025",
    "32-01-2022",
    "10-13-2024"
]

print("\n2. Date Validation:")

for date in dates:
    if re.fullmatch(pattern2, date):
        print(date, "-> Valid Format")
    else:
        print(date, "-> Invalid Format")


# --------------------------------------------------
# 3. Extract email addresses from text
# --------------------------------------------------

text = """
Contact us at john@gmail.com or support@example.com.
You can also email admin@test.org for more information.
"""

pattern3 = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

emails = re.findall(pattern3, text)

print("\n3. Email Addresses Found:")

for email in emails:
    print(email)