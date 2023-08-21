"""
A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is 1, 2, or 3 characters in length.
Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

Hint: Try using Email.utils() to complete this challenge. For example, this code:
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import email.utils
import re


def is_valid_email(email):
    pattern = r"^[a-zA-Z][a-zA-Z0-9_.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
    if re.match(pattern, email):
        return True
    return False


n = int(input())

for _ in range(n):
    parsed_email = email.utils.parseaddr(input())
    name, e_mail = parsed_email
    if is_valid_email(e_mail):
        print(email.utils.formataddr((name, e_mail)))
