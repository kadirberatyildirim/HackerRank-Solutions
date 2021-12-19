"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

    It must contain at least 2 uppercase English alphabet characters.
    It must contain at least 3 digits (0 - 9).
    It should only contain alphanumeric characters.
    No character should repeat.
    There must be exactly 10 characters in a valid UID.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

T = int(input())

cnt_upper = lambda string: sum(1 for c in string if c.isupper())
cnt_digit = lambda string: sum(c.isdigit() for c in string)

for _ in range(T):
    uid = str(input())
    
    #These conditions can be seperated to increase readability, though I have just written them in one line for this practice.
    if cnt_upper(uid) >= 2 and cnt_digit(uid) >= 3 and uid.isalnum() and all(i == 1 for i in Counter(uid).values()) and len(uid) == 10:
        print('Valid')
    else:
        print('Invalid')
    