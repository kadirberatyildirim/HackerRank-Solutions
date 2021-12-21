"""
Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers, 0 being the first number. 
Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.
"""

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0: return []
    elif n == 1: return [0]
    elif n == 2: return [0, 1]
    else:
        lst = fibonacci(n - 1)
        lst.append(lst[-1] + lst[-2])
        return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))