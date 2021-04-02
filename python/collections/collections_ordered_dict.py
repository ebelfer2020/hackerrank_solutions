# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

a_list=OrderedDict()

n = int(input())

for i in range(n):
    inp = input()
    
    if type(inp) !=int:
        isplit = inp.split()
        cost= isplit[-1]
        item = isplit[:-1]
        item = " ".join(item)
        cost = "".join(cost)
        cost = int(cost)

        if item in a_list:
            current=a_list[item]
            current +=cost
            a_list[item] = current
        else:
            a_list[item] = cost

for key, value in a_list.items():
    print (key, value)
