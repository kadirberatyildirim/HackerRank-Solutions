"""
You are given a 2-D array with dimensions NxM.
Your task is to perform the sum tool over axis 0 and then find the product of that result.
"""

import numpy as np

N, M = list(map(int, input().split()))

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    
print(np.prod(np.sum(np.array(arr), axis = 0)))