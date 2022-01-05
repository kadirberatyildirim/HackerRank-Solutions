"""
Students of District College have subscriptions to English and French newspapers. 
Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

eng = int(input())
roll_eng = list(map(int, input().split()))
fre = int(input())
roll_fre = list(map(int, input().split()))

set_eng, set_fre = set(roll_eng), set(roll_fre)

print(len(set_eng.symmetric_difference(set_fre)))