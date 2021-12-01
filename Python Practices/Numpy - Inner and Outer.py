"""
You are given two arrays: A and B.
Your task is to compute their inner and outer product.
"""

import numpy as np

A, B = (np.array(input().split(), dtype=int) for _ in range(2))

print(np.inner(A, B), np.outer(A, B), sep = '\n')

