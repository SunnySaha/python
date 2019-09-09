import numpy

a = int(input())
arr = numpy.array([input().split() for _ in range(a)], float)
print(numpy.around(numpy.linalg.det(arr), 2))
