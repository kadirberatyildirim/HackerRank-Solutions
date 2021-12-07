"""
An integer d is a divisor of an integer n if the remainder of n/d = 0.

Given an integer, for each digit that makes up the integer determine whether it is a divisor. 
Count the number of divisors occurring within the integer. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    get_digit = lambda number, n: number // 10**n % 10
    
    divisors = []
    for i in range(len(str(n))):
        digit = get_digit(n, i)
        if digit == 0:
            pass
        elif n % digit == 0:
            divisors.append(digit)

    return len(divisors)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
