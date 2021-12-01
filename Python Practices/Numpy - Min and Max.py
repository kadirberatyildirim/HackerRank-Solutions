"""
You are given a 2-D array with dimensions NxM.
Your task is to perform the min function over axis 1 and then find the max of that.
"""

import numpy as np

N, M = list(map(int, input().split()))

arr = []
for i in range(N):
    arr.append( list(map(int, input().split())) )

print(np.max(np.min(np.array(arr), axis = 1)))

