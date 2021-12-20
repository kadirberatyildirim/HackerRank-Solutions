"""
You are given a string S.
Your task is to find out whether S is a valid regex or not.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

T = int(input())

for _ in range(T):
    S = input()
    
    try:
        re.compile(S)
        print(True)
    
    except re.error:
        print(False)