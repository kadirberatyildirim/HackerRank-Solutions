"""
A random variable, X, follows Poisson distribution with mean of 2.5. 
Find the probability with which the random variable X is equal to 5.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import factorial, exp

miu = float(input())
x = int(input())
print(round( ((miu ** x) * exp(-miu)) / factorial(x), 3 ))