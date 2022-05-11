"""
Julius Caesar protected his confidential information by encrypting it using a cipher. 
Caesar's cipher shifts each letter by a number of letters. 
If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    import string
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    mapping = {lower[i]: lower[(i+k)%26] for i in range(26)}
    for i in range(len(mapping)):
        mapping[upper[i]] = upper[(i+k)%26]
    
    return ''.join([mapping[i] if i.isalpha() else i for i in s])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
