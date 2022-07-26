"""
Given a sequence of n integers, where each element is distinct and satisfies 1 <= p(x) <= n. 
For each x where 1 <= x <= n, that is x increments from 1 to n, find any integer y such that p(p(y)) = x 
and keep a history of the values of y in a return array.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    dic = {p[i]:i+1 for i in range(len(p))}
    return [dic[dic[i+1]] for i in range(len(p))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
