"""
The manager of a industrial plant is planning to buy a machine of either type A or type B. 
For each day’s operation:

    The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. 
    The daily cost of operating A is Ca = 160 + 40 X**2.
    The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. 
    The daily cost of operating B is Cb = 128 + 40 Y**2.

Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. 
Find and print the expected daily cost for each machine.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

meanA, meanB=map(float, input().split())

Ca= round(160 + 40 * (meanA + meanA**2), 3)
Cb= round(128 + 40 * (meanB + meanB**2), 3)

print(Ca, Cb, sep = '\n')