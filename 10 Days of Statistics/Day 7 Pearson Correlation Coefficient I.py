""""
Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
X = list(map(float,input().split()))
Y = list(map(float,input().split()))

mu_x, mu_y = sum(X) / n, sum(Y) / n

x_std = (sum([(i - mu_x)**2 for i in X]) / n)**0.5
y_std = (sum([(i - mu_y)**2 for i in Y]) / n)**0.5

covariance = sum([(X[i] - mu_x) * (Y[i] - mu_y) for i in range(n)])

coef = covariance / (n * x_std * y_std)

print(round(coef, 3))