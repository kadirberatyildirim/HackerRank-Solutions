"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    import itertools
    combinations = list(itertools.combinations(arr, 4))
    
    # Start with the first combination
    min_sum, max_sum = sum(combinations[0]), sum(combinations[0])
    for combination in combinations:
        sum_com = sum(combination)
        if sum_com < min_sum:
            min_sum = sum_com
        elif sum_com > max_sum:
            max_sum = sum_com
            
    print(str(min_sum), str(max_sum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
