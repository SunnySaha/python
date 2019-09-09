import numpy

n,m= map(int, input().split())
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.transpose(b))
print(b.flatten())