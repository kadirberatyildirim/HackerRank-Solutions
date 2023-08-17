"""
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. 
Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) 
with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import comb


def probability_of_a(n, letters, k):
    count_a = letters.count("a")

    non_a_combinations = comb(n - count_a, k)
    total_combinations = comb(n, k)
    P_not_a = non_a_combinations / total_combinations

    return 1 - P_not_a


if __name__ == "__main__":
    n = int(input().strip())
    letters = input().split()
    k = int(input().strip())

    result = probability_of_a(n, letters, k)
    print("{:.6f}".format(result))
