"""
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b, m = [int(input()) for i in range(3)]

print(a**b, pow(a, b, m), sep = '\n')