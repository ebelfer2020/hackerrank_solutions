# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import degrees, atan2

ab=int(input())
bc=int(input())

result = round(degrees(atan2(ab,bc)))
print (str(result)+ '°')
