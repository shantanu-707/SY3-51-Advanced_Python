import re

email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'


def find_emails(text):
    return re.findall(email_pattern, text)


def validate_email(email):
    return re.fullmatch(email_pattern, email) is not None



text = """
support@example.com, admin123@gmail.com
student.name@university.edu.
Invalid examples - abc@, @gmail.com and user@gmail.
"""

emails = find_emails(text)

print("Emails found:")
for email in emails:
    print(email)

test_emails = [
    "student@gmail.com",
    "john.doe@company.in",
    "abc@",
    "@gmail.com",
    "user@gmail",
    "hello123@yahoo.co.in"
]

print("\nEmail Validation:")

for email in test_emails:
    if validate_email(email):
        print(email, "-> Valid")
    else:
        print(email, "-> Invalid")