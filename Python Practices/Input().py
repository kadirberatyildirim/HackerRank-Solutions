"""
You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x)=k.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k = list(map(int, input().split()))

P = input().strip()

print(True if eval(P) == k else False)
