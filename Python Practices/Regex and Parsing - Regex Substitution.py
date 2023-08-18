"""
The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

def modify_text(text):
    modified_text = re.sub(r'(?<= )&&(?= )', 'and', text)
    modified_text = re.sub(r'(?<= )\|\|(?= )', 'or', modified_text)
    return modified_text

# Read the number of lines
n = int(input())

# Read and process each line
lines = []
for _ in range(n):
    line = input()
    modified_line = modify_text(line)
    lines.append(modified_line)

# Print the modified text
print('\n'.join(lines))
