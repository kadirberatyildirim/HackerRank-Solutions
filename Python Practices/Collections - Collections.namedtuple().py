"""
Dr. John Wesley has a spreadsheet containing a list of student's ID, Marks, Class and Name.

Your task is to help Dr. Wesley calculate the average marks of the students.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

N = int(input())
df = namedtuple('df', input())

summ = 0
for i in range(N):
    s = input().split()
    student = df(*s)
    
    summ += int(student.MARKS)
    
print(summ / N)