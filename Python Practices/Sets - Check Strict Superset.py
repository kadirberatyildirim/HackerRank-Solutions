"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset. 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(list(map(int, input().split())))
n = int(input())
result = False

for _ in range(n):
    other_set = set(list(map(int, input().split())))
    
    if A.issuperset(other_set) and len(A) > len(other_set):
        result = True
    else:
        result = False
        break
        
print(result)