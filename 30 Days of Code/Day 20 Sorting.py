"""
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. 
Once sorted, print the following 3 lines:

    Array is sorted in numSwaps swaps. where numSwaps is the number of swaps that took place.
    First Element: firstElement where firstElement is the first element in the sorted array.
    Last Element: lastElement where lastElement is the last element in the sorted array.
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    swaps = 0
    for i in range(0, n-1):
        for i in range(0, n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps +=1

    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}\nLast Element: {}".format(a[0], a[-1]))