# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input().split()
a =set(input().split())
b= set(input().split())

counter = 0

for i in m:
    if i in a:
        counter += 1
    if i in b:
        counter -= 1

print (counter)    
