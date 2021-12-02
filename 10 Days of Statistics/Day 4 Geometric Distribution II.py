"""
The probability that a machine produces a defective product is 1/3. 
What is the probability that the 1st defect is found during the first 5 inspections?
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT


prob = list(map(int, input().split()))
p = prob[0] / prob[1]

n = int(input())

q = 1-p

geo = 0
for i in range(1, n+1):
    geo += (q**(n-i)) * p
    
print(round(geo, 3))