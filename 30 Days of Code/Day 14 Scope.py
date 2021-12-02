"""
Complete the Difference class by writing the following:

    A class constructor that takes an array of integers as a parameter and saves it to the __elements instance variable.
    A computeDifference method that finds the maximum absolute difference between any 2 numbers in __elements and stores it in the maximumDifference instance variable. 
"""

class Difference:
    def __init__(self, a):
        self.__elements = a
        
    # Add your code here
    def computeDifference(self):
        from itertools import combinations
        
        self.maximumDifference = 0
        combination = list(combinations(self.__elements, 2))
        
        for comb in combination:
            diff = abs(comb[0]-comb[1])
            if diff > self.maximumDifference:
                self.maximumDifference = diff

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)