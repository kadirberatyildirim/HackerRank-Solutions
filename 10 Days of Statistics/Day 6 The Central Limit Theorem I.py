"""
A large elevator can transport a maximum of 9800 pounds. 
Suppose a load of cargo containing 49 boxes must be transported via the elevator. 
The box weight of this type of cargo follows a distribution with a mean of mu = 205 pounds and a standard deviation of sigma = 15 pounds. 
Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

x = int(input())
n = int(input())
mu = n * int(input())
sigma = math.sqrt(n) * int(input())

def central(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5 * (1 + math.erf(Z / (math.sqrt(2))))

print(round(central(x, mu, sigma), 4))