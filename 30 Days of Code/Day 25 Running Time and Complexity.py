"""
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
Given a number, n, determine and print whether it is Prime or Not prime.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

T = int(input())

for j in range(T):
    n = int(input())
    
    divisors = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if(n % i == 0) :
            if(n / i == i) :
                divisors.append(i)
            else :
                divisors.append(i)
                divisors.append(n/i)
            
    if len(divisors) == 2:
        print('Prime')
    else:
        print('Not prime')