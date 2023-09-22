"""
Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters. 
Lisa believes a problem to be special if its index (within a chapter) is the same as the page 
number where it's located. The format of Lisa's book is as follows:

There are n chapters in Lisa's workbook, numbered from 1 to n.
The ith chapter has arr[i] problems, numbered from 1 to arr[i].
Each page can hold up to k problems. Only a chapter's last page of exercises may contain fewer than k problems.
Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
The page number indexing starts at 1.
Given the details for Lisa's workbook, can you count its number of special problems?
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#


def workbook(n, k, arr):
    # Write your code here
    page = 1
    special_problems = 0

    for chapter in arr:
        for problem_num in range(1, chapter + 1):
            if problem_num == page:
                special_problems += 1
            if problem_num % k == 0 or problem_num == chapter:
                page += 1

    return special_problems


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + "\n")

    fptr.close()
