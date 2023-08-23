"""
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0).
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, 
    fine=15 Hackos x (the number of days late).
If the book is returned after the expected return month but still within the same calendar year as the expected return date, 
    the fine=500 Hackos x (the number of months late).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000.
Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, 
if it is returned January 1, 2018, that is a year late and the fine would be 10000.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#


def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    # If the book is returned before the due date, no fine will be charged.
    if y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 <= d2):
        return 0
    # If the book is returned after the calendar year in which it was expected.
    if y1 > y2:
        return 10000
    # If the book is returned after the expected return month but still within the same calendar year.
    if m1 > m2:
        return 500 * (m1 - m2)
    # If the book is returned after the expected return day but still within the same calendar month and year.
    return 15 * (d1 - d2)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + "\n")

    fptr.close()
