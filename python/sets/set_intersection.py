# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = int(input())

set_n = set(map(int, input().split()))

_ = int(input())

set_b = set(map(int, input().split()))

print (len(set_n & set_b))

