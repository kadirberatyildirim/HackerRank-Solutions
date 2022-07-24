
"""
There is an array of n integers. 
There are also 2 disjoint sets, A and B, each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
For each i integer in the array, if i in A, you add 1 to your happiness. If i in B, you add -1 to your happiness. 
Otherwise, your happiness does not change. Output your final happiness at the end. 
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = list(map(int, input().split()))
n_list = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print( sum([(i in A) - (i in B) for i in n_list]) )
