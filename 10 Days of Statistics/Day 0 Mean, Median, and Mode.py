"""
Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
If your array contains more than one modal value, choose the numerically smallest one.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

def getMode(list):
    mode = 0
    size = len(list)
    count, max = 0, 0
    copy = list
    copy.sort()
    current = 0
    for i in copy:
        if (i == current):
            count += 1
        else:
            count = 1
            current = i
        if (count > max):
            max = count
            mode = i
    return mode

N = int(input())

X = list(map(int, input().split()))

print( sum(X) / len(X) )

X.sort()
mid = len(X) // 2
res = (X[mid] + X[~mid]) / 2
print( res )

from collections import Counter
counts = Counter(X)

print(getMode(X))
