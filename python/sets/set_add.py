# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

names = set([])
for i in range(n):
    names.add(input())

print(len(names))

