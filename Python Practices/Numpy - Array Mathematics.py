"""
You are given two integer arrays, and of dimensions NxM.
Your task is to perform the following operations:
    Add 
    Subtract 
    Multiply 
    Integer Division 
    Mod 
    Power
"""

import numpy as np

N, M = list(map(int, input().split()))

A, B = (np.array([input().split() for _ in range(N)], dtype=int) for _ in range(2))
    
print(np.add(A, B), np.subtract(A, B), np.multiply(A, B), A//B, np.mod(A, B), np.power(A, B), sep = '\n')
