"""
Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.
"""

#!/bin/python3

import math
import os
import random
import re
import sys



S = input().strip()

try: 
    n = int(S) 
    print(n)
except ValueError: 
    print("Bad String")