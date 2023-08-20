"""
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    frequency = [0] * 101
    for num in a: frequency[num] += 1
    return max(frequency[i] + frequency[i + 1] for i in range(len(frequency) - 1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
