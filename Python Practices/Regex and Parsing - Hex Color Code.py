"""
You are given N lines of CSS code. 
Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom. 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())

check = False
for _ in range(N):
    code = str(input())
    
    if '{' in code: check = True
    elif '}' in code: check = False  
    elif check:
        for color in re.findall('#[0-9a-fA-F]{3,6}', code):
            print(color)