# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations
n = int(input())
letters = list(input().split(" "))
k = int(input())


tuples = list(combinations(letters, k))
contains = [word for word in tuples if "a" in word]
print (len(contains)/len(tuples))
