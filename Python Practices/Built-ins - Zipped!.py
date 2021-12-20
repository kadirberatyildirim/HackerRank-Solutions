"""
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = list(map(int, input().split()))
    
marks = [list(map(float, input().split())) for _ in range(X)]
sep_marks = list(zip(*marks))

print( *["{:.1f}".format(sum(i)/len(i)) for i in sep_marks], sep = '\n')
