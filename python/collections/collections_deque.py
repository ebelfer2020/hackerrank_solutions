# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

d = deque()

for _ in range (int(input())):
    oper, val, *args = input().split() + ['']
    eval (f'd.{oper} ({val})')

print(*d)

