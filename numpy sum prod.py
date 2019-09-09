import numpy
a, b = map(int, input().split())
arr = numpy.array([input().split() for _ in range(a)], int)
sum = numpy.sum(arr, axis=0)
print(numpy.prod(sum))