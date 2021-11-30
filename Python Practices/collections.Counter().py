"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay x_i amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())

shoe_sizes = list(map(int, input().split()))
shoe_size_counts = Counter(shoe_sizes)

earned = 0

N = int(input())
for i in range(N):
    order = list(map(int, input().split()))
    
    if shoe_size_counts[order[0]] > 0:
        shoe_size_counts[order[0]] -= 1
        earned += order[1]

print(earned)