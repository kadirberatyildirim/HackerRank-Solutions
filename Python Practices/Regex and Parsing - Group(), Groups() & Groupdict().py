"""
You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions. 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = str(input())

m = re.search(r"([a-zA-Z0-9])\1+", S)

print(m.group(1) if m else -1)