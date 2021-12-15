"""
Perform append, pop, popleft and appendleft methods on an empty deque d.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

N = int(input())

d = deque()

for _ in range(N):
    operation = str(input())
    
    try:
        op, num = operation.split()
        eval('d.' + op + '(' + num + ')')
    except:
        eval('d.' + operation + '()')
        
print(*d)