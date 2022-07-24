
"""
You are given a string S.
S contains alphanumeric characters only.

Your task is to sort the string S in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

S = str(input())

low, up, odd, eve = [], [], [], []
for char in sorted(S):
    if char.isalpha():
        if char.islower(): low.append(char)
        else: up.append(char)
    elif char.isnumeric():
        if int(char) % 2 != 0: odd.append(char)
        else: eve.append(char)
        
print("".join(low + up + odd + eve))