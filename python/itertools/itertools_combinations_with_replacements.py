# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, k = map(str, input().split())

s = sorted(s)
k = int(k)

for x in list(combinations_with_replacement(s,k)):
    print(*x, sep='')

