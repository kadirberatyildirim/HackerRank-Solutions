"""
You are given a string N.
Your task is to verify that N is a floating point number. 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

T = int(input())

regex = r'^[-+]?[0-9]*\.[0-9]+$'

for _ in range(T):
    N = str(input())
    
    if re.search(regex, N): print(True)
    else: print(False)