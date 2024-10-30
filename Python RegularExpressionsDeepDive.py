import re

# Task: Define sample text with email addresses
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Task: Extract all email addresses except those from 'exclude.com'
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com\b)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

# Task: Output the list of valid extracted emails
print(emails)
