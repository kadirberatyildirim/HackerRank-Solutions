"""
Students of District College have a subscription to English and French newspapers. 
Some students have subscribed to only the English newspaper, 
some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, 
nd one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to only English newspapers.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

num_eng = int(input())
roll_eng = list(map(int, input().split()))
num_fre = int(input())
roll_fre = list(map(int, input().split()))

set_eng, set_fre = set(roll_eng), set(roll_fre)

print(len(set_eng.difference(set_fre)))