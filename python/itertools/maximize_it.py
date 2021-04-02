# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

number_of_lists, modulus = map(int, input().split())
list_of_lists = []

for i in range(0, number_of_lists):
    new_list = list(map(int, input().split()))
    del new_list[0]
    list_of_lists.append(new_list)
    
def squared(element):
    return element**2

combs = list(itertools.product(*list_of_lists))
results =[]

for i in combs:
    results1 = sum(map(squared, [a for a in i]))
    results2 = results1 % modulus
    results.append(results2)
    
print(max(results))
