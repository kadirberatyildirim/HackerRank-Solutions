"""
In a certain plant, the time taken to assemble a car is a random variable, X, 
having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. 
What is the probability that a car can be assembled at this plant in:

    Less than 19.5 hours?
    Between 20 and 22 hours?
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

mean, sd = map(float, input().split())
x = float(input())
y1, y2 = map(float, input().split())

def normalDistribution(x, mean, sd):
    return round(0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5)))), 3)

print(normalDistribution(x, mean, sd))
print(normalDistribution(y2, mean, sd) - normalDistribution(y1, mean, sd))