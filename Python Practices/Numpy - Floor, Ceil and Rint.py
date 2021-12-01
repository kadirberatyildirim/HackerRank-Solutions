"""
You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A. 
"""

import numpy as np
np.set_printoptions(legacy = '1.13')

arr = np.array( list(map(float, input().split())) )

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))

