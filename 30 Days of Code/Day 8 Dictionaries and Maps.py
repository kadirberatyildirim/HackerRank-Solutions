"""
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
You will then be given an unknown number of names to query your phone book for. 
For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
if an entry for name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure. 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(input())

dictt = {}

for i in range(x):
    text = input().split()
    dictt[text[0]] = text[1]

while True:
    try:
        inpt = input()
        if inpt in dictt:
            print(inpt+"="+dictt[inpt])
        else:
            print("Not found")
    except EOFError:
        break
        