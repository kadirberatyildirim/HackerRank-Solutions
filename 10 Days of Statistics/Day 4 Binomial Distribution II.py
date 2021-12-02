"""
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. 
What is the probability that a batch of 10 pistons will contain:
    No more than 2 rejects?
    At least 2 rejects?
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

fact = lambda x: 1 if x == 0 else x * fact(x-1)

comb = lambda n, x: fact(n) / (fact(x) * fact(n-x))

binomial = lambda x, n, p: comb(n, x) * p**x * (1-p)**(n-x)

p, n = list(map(int, input().split(" ")))
print(round(sum([binomial(i, n, p/100) for i in range(3)]), 3))
print(round(sum([binomial(i, n, p/100) for i in range(2, n+1)]), 3))
