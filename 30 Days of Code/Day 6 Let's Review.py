"""
Given a string, S, of length N that is indexed from 0 to N-1, 
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail). 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    S = str(input())
    print(S[0::2] + " " + S[1::2])


