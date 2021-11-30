"""
You are given two arrays A and B. Both have dimensions of NxN.
Your task is to compute their matrix product.
"""

import numpy as np

N = int(input())

A = np.array([list(map(int, input().split())) for i in range(N)])
B = np.array([list(map(int, input().split())) for i in range(N)])
    
print( np.dot(A, B) )
