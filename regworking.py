import re

# --------------------------------------------------
# 1. Extract all email addresses
# --------------------------------------------------

text = """
Please contact john@gmail.com, support@example.com,
admin@test.org or developer@company.in for more information.
"""

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

emails = re.findall(email_pattern, text)

print("1. Email Addresses:")
for email in emails:
    print(email)


# --------------------------------------------------
# 2. Validate phone number
# Format: (123) 456-7890
# --------------------------------------------------

phone_pattern = r"^\(\d{3}\) \d{3}-\d{4}$"

phone_numbers = [
    "(123) 456-7890",
    "(987) 654-3210",
    "123-456-7890",
    "(123)456-7890"
]

print("\n2. Phone Number Validation:")

for phone in phone_numbers:
    if re.fullmatch(phone_pattern, phone):
        print(phone, "-> Valid")
    else:
        print(phone, "-> Invalid")


# --------------------------------------------------
# 3. Replace multiple whitespace characters
#    with a single space
# --------------------------------------------------

paragraph = """
Python    is a powerful     programming language.
Regular    expressions   are useful for text processing.
"""

clean_text = re.sub(r"\s+", " ", paragraph).strip()

print("\n3. Text After Removing Extra Spaces:")
print(clean_text)