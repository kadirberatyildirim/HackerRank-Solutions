"""
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

string = list(map(str, input().split()))

from itertools import combinations

for i in range(1, int(string[1]) + 1):
    for j in combinations(sorted(string[0]), i):
        print (''.join(j))