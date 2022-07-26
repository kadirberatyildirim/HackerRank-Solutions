"""
You are given a number of sticks of varying lengths. 
You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. 
At each iteration you will determine the length of the shortest stick remaining, 
cut that length from each of the longer sticks and then discard all the pieces of that shortest length. 
When all the remaining sticks are the same length, they cannot be shortened so discard them.

Given the lengths of n sticks, print the number of sticks that are left before each iteration until there are none left.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    lens = []
    while len(arr) >= 1:
        lens.append(len(arr))
        minn = min(arr)
        while minn in arr: arr.pop(arr.index(minn))
        arr = [num - minn for num in arr]
    return lens

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
