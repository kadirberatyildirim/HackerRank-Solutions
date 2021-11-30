"""
Given an array, arr, of n integers, calculate the respective first quartile, second quartile, and third quartile. It is guaranteed that they are integers. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def find_median(arr):
    if len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) // 2

def quartiles(arr):
    # Write your code here
    arr.sort()
    
    result = []
    
    result.append(find_median(arr[:len(arr)//2]))
    
    if len(arr)%2 != 0:
        result.append(find_median(arr))
    elif len(arr)%2 == 0:
        result.append(find_median(arr))
        
    result.append(find_median(arr[len(arr) // 2 + len(arr) % 2:]))
                    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
