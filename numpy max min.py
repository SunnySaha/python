import numpy

a, b = map(int, input().split())

arr = numpy.array([input().split() for _ in range(a)], int)

min = numpy.min(arr, axis=1)
print(numpy.max(min))