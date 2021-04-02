# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

number_of_shoes = int(input())
sizes_in_stock = collections.Counter(map(int, input().split()))

revenue =0

for _ in range (int(input())):
    size, price = map(int, input().split())
    if sizes_in_stock[size]:
        revenue += price
        sizes_in_stock[size] -= 1

print (revenue)
