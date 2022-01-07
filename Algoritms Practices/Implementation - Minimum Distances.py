"""
The distance between two array values is the number of indices between them. 
Given a, find the minimum distance between any pair of equal elements in the array. 
If no such value exists, return -1.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    dup_idx = [ idx for idx, val in enumerate(a) if val in a[:idx] ]
    
    diff = [ idx2 - idx1 for idx1, value in enumerate(a) for idx2 in dup_idx if value == a[idx2] ]
    
    return min([i for i in diff if i > 0]) if sum(diff) != 0 else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
