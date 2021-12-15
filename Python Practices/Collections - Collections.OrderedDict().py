"""
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

N = int(input())

items = [input() for _ in range(N)]
dic = OrderedDict()

for item in items:
    price = int(item.split()[-1])
    name = " ".join(item.split()[:-1])
    
    if(dic.get(name)): dic[name] += price
    else: dic[name] = price
    
[print(i + ' ' + str(dic[i]), sep = '\n') for i in dic.keys()]