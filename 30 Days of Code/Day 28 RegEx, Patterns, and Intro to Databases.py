"""
Consider a database table, Emails, which has the attributes First Name and Email ID. 
Given N rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com.
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    regex = re.compile(r"@gmail\.com$")
    
    names = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        
        if regex.search(emailID):
            names.append(firstName)
            
    names.sort()
        
    print(*names, sep = '\n')

        
    
        
    