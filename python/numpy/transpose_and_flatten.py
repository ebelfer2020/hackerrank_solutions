import numpy

n, m = map(int, input().split())

lines =[]

array = numpy.array([input().strip().split() for _ in range(n)], int)

print (array.transpose())
print (array.flatten())
