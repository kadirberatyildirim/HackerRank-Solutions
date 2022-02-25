"""
You are given a string S. 
Suppose a character 'c' occurs consecutively X times in the string. 
Replace these consecutive occurrences of the character 'c' with (X, c) in the string. 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

S = str(input())

print( *[(len(list(g)), int(k)) for k, g in groupby(S)] )



