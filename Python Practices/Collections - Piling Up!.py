"""
There is a horizontal row of n cubes. The length of each cube is given. 
You need to create a new vertical pile of cubes. The new pile should 
follow these directions: if cube[i] is on top of cube[j] then sideLength[j]>=sideLengh[i].

When stacking the cubes, you can only pick up either the leftmost or 
the rightmost cube each time. Print Yes if it is possible to stack 
the cubes. Otherwise, print No.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))

    prev = float("inf")
    while blocks:
        if len(blocks) == 1 or (blocks[0] <= prev and blocks[0] >= blocks[-1]):
            curr = blocks.pop(0)
        else:
            curr = blocks.pop()

        if curr > prev:
            print("No")
            break
        prev = curr
    else:
        print("Yes")
