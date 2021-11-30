"""
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

string = list(map(str, input().split()))

from itertools import permutations

for permutation in sorted(list(permutations(string[0], int(string[1])))):
    print(''.join(permutation))