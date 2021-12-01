"""
You are given a square matrix A with dimensions NxN. 
Your task is to find the determinant. 
Note: Round the answer to 2 places after the decimal.
"""

import numpy as np

N = int(input())

A = np.array([list(map(float, input().split())) for _ in range(N)])

print(np.around(np.linalg.det(A), decimals=2))