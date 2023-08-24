"""
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. 
He wants to verify whether his credit card numbers are valid or not. You happen to be great 
at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


def is_valid(card):
    # Remove hyphens
    card = card.replace("-", "")

    # Must start with 4, 5 or 6
    if not re.match("^[4-6]", card):
        return "Invalid"

    # Must have exactly 16 digits
    if not re.match("^\d{16}$", card):
        return "Invalid"

    # Must not have 4 or more consecutive repeated digits
    if re.search(r"(\d)(\1{3,})", card):
        return "Invalid"

    return "Valid"


# Input number of cards
n = int(input().strip())

for _ in range(n):
    card = input().strip()

    # Check if card has valid format and valid characters only
    if re.match("^[4-6]\d{3}(-?\d{4}){3}$", card) and not re.search(r"[^\d-]", card):
        print(is_valid(card))
    else:
        print("Invalid")
