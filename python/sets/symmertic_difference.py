# Enter your code here. Read input from STDIN. Print output to STDOUT
#data input
m = int(input())
a=set(map(int, input().split()))
n = int(input())
b=set(map(int, input().split()))

#Difference in each sets
c= a.difference(b)
d =b.difference(a)

#Union of the difference
e=c.union(d)

#Converting set to a list
result =list(e)

#sorting
result.sort()

#iteration
for i in range(len(result)):
    print(result[i])

