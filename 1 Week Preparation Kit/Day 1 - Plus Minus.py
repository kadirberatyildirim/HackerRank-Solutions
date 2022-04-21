"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = len([i for i in arr if i > 0]) / len(arr)
    zero = len([i for i in arr if i == 0]) / len(arr)
    neg = len([i for i in arr if i < 0]) / len(arr)
    
    print(*["{:.6f}\n".format(i) for i in [pos, neg, zero]])

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
