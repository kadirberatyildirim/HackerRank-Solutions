"""
Given two n-element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

def rank(X, n):
    x_rank = dict((x, i+1) for i, x in enumerate(sorted(set(X))))
    return [x_rank[x] for x in X]
    
n = int(input())
X, Y = [list(map(float, input().split())) for i in range(2)]

rx, ry = rank(X, n), rank(Y, n)

d = [(rx[i] - ry[i])**2 for i in range(n)]
rxy = 1 - (6 * sum(d)) / (n * (n*n - 1))

print(round(rxy, 3))