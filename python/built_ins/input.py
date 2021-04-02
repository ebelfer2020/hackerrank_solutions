# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = map(int, input().split())
expr = input()

print (eval(expr) == k)
