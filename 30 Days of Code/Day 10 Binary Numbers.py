"""
Given a base-10 integer, convert it to binary (base-2). 
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. 
When working with different bases, it is common to show the base as a subscript. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    n_bin = "{0:b}".format(n)
    
    print(len(max(n_bin.split('0'), key=len)))
        