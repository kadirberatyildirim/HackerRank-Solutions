"""
The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution 
that has a mean of mu = 2.4 and a standard deviation of sigma = 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. 
If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

numTic = float(input())
numStd = float(input())
mu = numStd * float(input())
sig = math.sqrt(numStd) * float(input())

print(round(0.5 * (1 + math.erf((numTic - mu) / (sig * math.sqrt(2)))), 4))