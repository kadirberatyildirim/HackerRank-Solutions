"""
The final grades for a Physics exam taken by a large group of students have a mean of mu = 70 
and a standard deviation of sigma = 10. 
If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

    Scored higher than 80)?
    Passed the test?
    Failed the test?

Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

mean, sd = map(float, input().split())
x, y = int(input()), int(input())

def normalDistribution(x, mean, sd):
    return round(0.5 * 100 * (1 + math.erf((x - mean) / (sd * math.sqrt(2)))), 3)

print(round(100 - normalDistribution(x, mean, sd), 2))
print(round(100 - normalDistribution(y, mean, sd), 2))
print(round(normalDistribution(60, 70, 10), 2))