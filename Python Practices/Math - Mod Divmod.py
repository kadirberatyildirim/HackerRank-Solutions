"""
Read in two integers, a and b, and print three lines.
The first line is the integer division a//b (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: a%b.
The third line prints the divmod of a and b. 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b = [int(input()) for i in range(2)]

print(a//b, a%b, divmod(a, b), sep = '\n')