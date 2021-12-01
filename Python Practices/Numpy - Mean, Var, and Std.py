"""
You are given a 2-D array of size NxM.

Your task is to find:
    The mean along axis 1
    The var along axis 0
    The std along axis None
"""

import numpy as np

N, M = list(map(int, input().split()))

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    
arr = np.array(arr)

print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(np.around(np.std(arr, axis = None), decimals = 11))