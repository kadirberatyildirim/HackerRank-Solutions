"""
There is a string, s, of lowercase English letters that is repeated infinitely many times. 
Given an integer, n, find and print the number of letter a's in the first letters of the infinite string.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code her
    #This one exceeds time limit on some cases
    #return sum([ True for i in range(n) if s[i % len(s)] == 'a' ])
    #This one solves it better:
    return int(s.count('a') * (n - n % len(s)) / len(s) + s[:n % len(s)].count('a'))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
