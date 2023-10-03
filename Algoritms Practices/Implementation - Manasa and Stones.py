"""
Manasa is out on a hike with friends. 
She finds a trail of stones with numbers on them. She starts following the trail and notices that any two consecutive stones' 
numbers differ by one of two values. Legend has it that there is a treasure trove at the end of the trail. If Manasa can guess 
the value of the last stone, the treasure will be hers.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#


def stones(n, a, b):
    # Write your code here
    return sorted(set([a * i + b * (n - 1 - i) for i in range(n)]))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(" ".join(map(str, result)))
        fptr.write("\n")

    fptr.close()
