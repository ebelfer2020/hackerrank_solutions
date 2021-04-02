# Enter your code here. Read input from STDIN. Print output to STDOUT

#Number of elements in set a
a=int(input())

#Get Set A
set_a = set(map(int, input().split()))

#Number of other sets
n = int(input())

# Loop through other sets
for _ in range(n):
    operation = input().split()
    new_set = set(map(int, input().split())) # Get set
    eval('set_a.{}({})'.format(operation[0], new_set))

print (sum(set_a))

