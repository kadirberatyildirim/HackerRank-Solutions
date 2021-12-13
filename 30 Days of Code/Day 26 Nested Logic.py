"""
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). 
The fee structure is as follows:

    If the book is returned on or before the expected return date, no fine will be charged.
    If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 Hackos x (# of days late).
    If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 Hackos x (# of months late).
    If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

day_returned, month_returned, year_returned = list(map(int, input().split()))
day_expected, month_expected, year_expected = list(map(int, input().split()))

fine = 0
if year_returned > year_expected:
    fine = 10000
elif year_returned == year_expected and month_returned > month_expected:
    fine = 500 * (month_returned - month_expected)
elif year_returned == year_expected and month_returned == month_expected and day_returned > day_expected:
    fine = 15 * (day_returned - day_expected)

print(fine)