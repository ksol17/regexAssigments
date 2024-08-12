# Task 1: Email Extraction Enhancement

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Regular expression to find email addresses excluding those from 'exclude.com'
pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Extracting email addresses using the re.findall() function
emails = re.findall(pattern, text)

# Printing the extracted email addresses
print("Extracted emails (excluding 'exclude.com'):")
for email in emails:
    print(email)
