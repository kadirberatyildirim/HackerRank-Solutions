"""
A child is playing a cloud hopping game. 
In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. 
The character must jump from cloud to cloud until it reaches the start again.

There is an array of clouds, c and an energy level e = 100. The character starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud c[i+k]%n. 
If it lands on a thundercloud, c[i] = 1, its energy (e) decreases by 2 additional units. 
The game ends when the character lands back on cloud 0.

Given the values of n, k, and the configuration of the clouds as an array c, determine the final value of after the game ends.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    cloud, energy = 0, 100
    
    cloud = k if k < len(c) else k - len(c)
    energy -= 1 if c[cloud] == 0 else 3
    
    while cloud != 0:
        cloud = cloud+k if cloud+k < len(c) else cloud+k - len(c)
        energy -= 1 if c[cloud] == 0 else 3
        
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
