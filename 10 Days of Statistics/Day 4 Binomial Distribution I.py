"""
The ratio of boys to girls for babies born in Russia is 1.09:1. 
If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

fact = lambda x: 1 if x == 0 else x * fact(x-1)

comb = lambda n, x: fact(n) / (fact(x) * fact(n-x))

binomial = lambda x, n, p: comb(n, x) * p**x * (1-p)**(n-x)

l, r = list(map(float, input().split(" ")))
odds = l / r
print(round(sum([binomial(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))