"""
You are given a function f(X) = X^2. You are also given K lists. The ith list consists of N_i elements.

You have to pick one element from each list so that the value from the equation below is maximized:

S=(f(X_1)+f(X_2)+...+f(X_k))%M

X_i denotes the element picked from the ith list . Find the maximized value S_max obtained.

% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. 
You add the squares of the chosen elements and perform the modulo operation. The maximum value that 
you can obtain, will be the answer to the problem.


"""

# Enter your code here. Read input from STDIN. Print output to STDOUT


def maximize(lists, M, current_sum=0, index=0):
    # If we're at the last list
    if index == len(lists):
        return current_sum % M

    max_val = 0
    for num in lists[index]:
        max_val = max(max_val, maximize(lists, M, current_sum + num * num, index + 1))

    return max_val


N, M = map(int, input().split())

lists = []
for _ in range(N):
    _, *lst = map(int, input().split())
    lists.append(lst)


print(maximize(lists, M))
