"""
You are given n words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification. 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

def word_occurrences(input_lines):
    n = int(input_lines[0])
    words = input_lines[1:]
    
    word_count = {}
    distinct_words = []
    
    for word in words:
        word = word.strip()
        if word not in word_count:
            word_count[word] = 1
            distinct_words.append(word)
        else:
            word_count[word] += 1
    
    distinct_word_count = len(distinct_words)
    occurrences = [word_count[word] for word in distinct_words]
    
    return distinct_word_count, occurrences

# Read input
input_lines = []
try:
    while True:
        line = input()
        input_lines.append(line)
except EOFError:
    pass

# Calculate word occurrences
distinct_word_count, occurrences = word_occurrences(input_lines)

# Print output
print(distinct_word_count)
print(" ".join(str(occ) for occ in occurrences))
