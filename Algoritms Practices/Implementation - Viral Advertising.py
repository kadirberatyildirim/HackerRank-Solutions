"""
HackerLand Enterprise is adopting a new viral advertising strategy. 
When they launch a new product, they advertise it to exactly 5 people on social media.

On the first day, half of those 5 people like the advertisement and each shares it with 3 of their friends. 
At the beginning of the second day, floor(5/2)*3 = 2*3 = 6 people receive the advertisement.

Each day, floor(recipients / 2) of the recipients like the advertisement and will share it with 3 friends on the following day. 
Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    people, result = 5, 0
    
    for _ in range(n):
        half = people // 2
        result += half
        people = 3 * half
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
