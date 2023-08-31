"""
A driver is driving on the freeway. The check engine light of his 
vehicle is on, and the driver wants to get service immediately. 
Luckily, a service lane runs parallel to the highway. It varies in 
width along its length.

You will be given an array of widths at points along the road (indices), 
then a list of the indices of entry and exit points.
Considering each entry and exit point pair, calculate the maximum 
size vehicle that can travel that segment of the service lane safely.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#


def serviceLane(n, cases):
    # Write your code here
    return [min(width[start : end + 1]) for start, end in cases]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
