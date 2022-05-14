"""
We define super digit of an integer x using the following rules:

Given an integer, we need to find the super digit of the integer.

    If x has only digit, then its super digit is x.
    Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    num = int( str(n) * k )
    while len(str(num)) != 1:
        num = sum([int(i) for i in list(str(num))])
    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
