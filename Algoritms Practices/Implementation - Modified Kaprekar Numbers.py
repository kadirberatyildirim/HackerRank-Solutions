"""
A modified Kaprekar number is a positive whole number with a special property. 
If you square it, then split the number into two integers and sum those integers, you have the same value you started with.

Consider a positive whole number n with d digits. 
We square to arrive at a number that is either 2xd digits long or (2xd)-1 digits long. 
Split the string representation of the square into two parts, l and r. 
The right hand part, r must be d digits long. The left is the remaining substring. 
Convert those two substrings back to integers, add them and see if you get n.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    kaprekars = []
    for num in range(p, q+1):
        sq = str(num**2)
        d = len(str(num))
        r = sq[len(sq) - d:]
        l = sq[:len(sq) - d]
        if r == '': r = 0
        if l == '': l = 0
        if int(r) + int(l) == num: kaprekars.append(num)
    if kaprekars: print(" ".join(str(x) for x in kaprekars))
    else: print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
