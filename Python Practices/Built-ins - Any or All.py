"""
You are given a space separated list of integers. 
If all the integers are positive, then you need to check if any integer is a palindromic integer.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
nums = list(map(int, input().split()))
    
isPalindrome = lambda num: str(num) == str(num)[::-1]

if all(i > 0 for i in nums):
    print(any(isPalindrome(i) for i in nums))
else:
    print(False)