"""
Given a sequence of integers a, a triplet (a[i], a[j], a[k]) is beautiful if:

* i<j<k
* a[j]-a[i]=a[k]-a[j]=d

Given an increasing sequenc of integers and the value of d, 
count the number of beautiful triplets in the sequence.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#


def beautifulTriplets(d, arr):
    # Write your code here
    numbers = set(arr)
    return sum(1 for i in arr if i + d in numbers and i + 2 * d in numbers)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + "\n")

    fptr.close()
