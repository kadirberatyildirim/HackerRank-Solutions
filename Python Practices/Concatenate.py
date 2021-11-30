"""
You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column). 
Your task is to concatenate the arrays along axis 0.
"""

import numpy as np

N, M, P = list(map(int, input().split()))

A = np.array([list(map(int, input().split())) for i in range(N)])
B = np.array([list(map(int, input().split())) for i in range(M)])

print(np.concatenate((A, B), axis = 0))